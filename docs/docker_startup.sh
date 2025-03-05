#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

PORT=${PORT:-8000}

echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 8 --timeout 0 docs.wsgi
