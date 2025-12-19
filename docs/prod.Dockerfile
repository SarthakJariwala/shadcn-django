# Stage 1: Build Tailwind CSS
FROM node:20-slim AS css-builder
WORKDIR /code
COPY package.json package-lock.json ./
RUN npm ci
COPY static/css/input.css static/css/input.css
RUN npx @tailwindcss/cli -i static/css/input.css -o static/css/output.css --minify

# Stage 2: Build the Python application using uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS python-builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /code
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project --no-dev
ADD . /code
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

# Stage 3: Use the final image without uv
# It is important to use the image that matches the python-builder, as the path to the
# Python executable must be the same, e.g., using `python:3.11-slim-bookworm`
# will fail.
FROM python:3.12-slim-bookworm

# Place executables in the environment at the front of the path
ENV PATH="/code/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0

RUN apt-get update \
    && apt-get install -y \
    curl \
    libpq-dev \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Copy the application from the builders
COPY --from=python-builder /code /code
COPY --from=css-builder /code/static/css/output.css /code/static/css/output.css

WORKDIR /code
COPY --chown=django:django . /code

# Remove input.css to prevent WhiteNoise from processing uncompiled Tailwind imports
RUN rm -f /code/static/css/input.css

RUN DEBUG=False python ./manage.py collectstatic --noinput --settings=docs.settings_production
RUN chown django:django -R staticfiles

USER django

COPY --chown=django:django docker_startup.sh /start
RUN chmod +x /start
CMD /start
