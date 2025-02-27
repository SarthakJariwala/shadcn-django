from typing import Annotated

import copier
import typer
from rich.status import Status

from .components import dependencies
from .console import console
from .constants import COMPONENTS_REPO_URL, DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True)


def get_component_dependencies(component: str) -> list[str]:
    """Fetch dependencies for the given component"""
    return dependencies.get(component, [])


@app.command(name="add")
def add(
    component: Annotated[
        str, typer.Argument(help="Name of the component to add")
    ],
    overwrite: Annotated[
        bool, typer.Option(help="Overwrite existing component files")
    ] = True,
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
            overwrite=overwrite,
        )

    for comp in components_to_install:
        console.print(
            f"[bold green]:heavy_check_mark: Added {comp} component successfully![/]",
        )
