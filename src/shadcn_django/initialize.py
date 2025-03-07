from pathlib import Path

import copier
import typer
from rich.panel import Panel
from rich.status import Status

from .console import console
from .constants import COMPONENTS_REPO_URL, DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command(name="init")
def init():
    """
    Initialize setup for shadcn_django components
    """
    DEFAULT_COMPONENTS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    with Status("Adding tailwind config for shadcn components"):
        copier.run_copy(
            src_path=COMPONENTS_REPO_URL,
            dst_path=Path.cwd(),
            vcs_ref="main",
            exclude=["*", "!tailwind.config.js", "!input.css"],
        )
    console.print(
        Panel(
            "[bold green]"
            ":rocket: Initialized shadcn_django components!\n\n"
            ":heavy_check_mark: Created "
            + f"'{DEFAULT_COMPONENTS_DIRECTORY}'\n"
            ":heavy_check_mark: Added TailwindCSS config required for shadcn components\n\n"
            "[/bold green]"
            "[bold yellow]"
            ":bookmark_tabs: Next steps:\n"
            "[/bold yellow]"
            ":arrow_right_hook: Ensure you have tailwind v4 and alpine.js installed\n"
            ":arrow_right_hook: Add <link rel='stylesheet' href='{% static 'css/output.css' %}'> to your base HTML template\n"
            ":arrow_right_hook: Run 'npx @tailwindcss/cli -i input.css -o static/css/output.css --watch'\n",
            title="Initialization Complete",
            border_style="bold green",
        )
    )
