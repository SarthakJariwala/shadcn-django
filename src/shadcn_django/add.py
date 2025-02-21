import importlib.resources
from typing import Annotated

import copier
import tomllib
import typer
from rich.status import Status

from .console import console
from .constants import COMPONENTS_REPO_URL, DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True)


def get_component_dependencies(component: str) -> list[str]:
    """Read components.toml file and fetch dependencies for the given component"""

    with importlib.resources.open_text("shadcn_django", "components.toml") as f:
        components = tomllib.loads(f.read())

    return components.get("dependencies", {}).get(component, [])


@app.command(name="add")
def add(
    component: Annotated[
        str, typer.Argument(help="Name of the component to add")
    ],
):
    """
    Add a new shadcn_django component to your project
    """

    component_dependencies = get_component_dependencies(component)
    components_to_install = {component}

    if component_dependencies:
        for dependency in component_dependencies:
            components_to_install.add(dependency)

    # exclude format: ["*", "!component", "!component.html"]
    component_excludes = [
        item
        for component in components_to_install
        for item in [f"!{component}", f"!{component}.html"]
    ]
    excludes = ["*"] + component_excludes

    with Status(f"Adding {component} component"):
        copier.run_copy(
            src_path=COMPONENTS_REPO_URL,
            dst_path=DEFAULT_COMPONENTS_DIRECTORY,
            vcs_ref="main",
            exclude=excludes,
        )

    console.print(
        f"[bold green]:heavy_check_mark: Added {component} component successfully![/]",
    )
