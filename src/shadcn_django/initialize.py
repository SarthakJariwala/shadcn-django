import typer
from rich.panel import Panel

from .console import console
from .constants import DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command(name="init")
def init():
    """
    Initialize a new project
    """
    DEFAULT_COMPONENTS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    console.print(
        Panel(
            ":rocket: Initialized directory structure for shadcn_django components!\n\n"
            ":heavy_check_mark: Created " + f"'{DEFAULT_COMPONENTS_DIRECTORY}'",
            title="Initialization Complete",
            style="bold green",
            border_style="bold green",
        )
    )
