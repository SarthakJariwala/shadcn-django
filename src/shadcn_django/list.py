import typer
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

from .components import dependencies
from .console import console

app = typer.Typer(no_args_is_help=True)


def get_all_components() -> list[str]:
    """Fetch all available components"""
    return list(dependencies.keys())


@app.command(name="list")
def list_components():
    """List all available components"""
    components = get_all_components()

    # Create styled component items and pretty print using Panel
    styled_components = [
        Text(component, style="green") for component in sorted(components)
    ]

    columns = Columns(styled_components, column_first=False, padding=(0, 2))

    panel = Panel(
        columns,
        title="[bold blue]Available Components",
        subtitle=f"[bold cyan]Total: {len(components)} components",
        box=box.ROUNDED,
        border_style="blue",
        padding=(1, 2),
    )

    console.print(panel)
