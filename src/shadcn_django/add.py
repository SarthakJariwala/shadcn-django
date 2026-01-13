import shutil
import tempfile
from pathlib import Path
from typing import Annotated

import copier
import typer
from rich.status import Status

from .components import dependencies
from .console import console
from .constants import COMPONENTS_REPO_URL, DEFAULT_COMPONENTS_DIRECTORY

app = typer.Typer(no_args_is_help=True)

# Components that install to templates/ root instead of templates/cotton/
# Maps component name to destination folder name (if different from component name)
TEMPLATE_ROOT_COMPONENTS = {
    "allauth": "account",  # allauth component installs to templates/account/
}


def get_component_dependencies(component: str) -> list[str]:
    """Fetch dependencies for the given component"""
    return dependencies.get(component, [])


def _install_component(
    components_to_install: set[str],
    overwrite: bool,
) -> None:
    """Install a component and its dependencies."""
    # Separate components by destination
    cotton_components = components_to_install - set(TEMPLATE_ROOT_COMPONENTS.keys())
    root_components = components_to_install & set(TEMPLATE_ROOT_COMPONENTS.keys())

    # Install cotton components (UI components)
    if cotton_components:
        component_excludes = [f"!{comp}" for comp in cotton_components]
        excludes = ["*"] + component_excludes

        copier.run_copy(
            src_path=COMPONENTS_REPO_URL,
            dst_path=DEFAULT_COMPONENTS_DIRECTORY,
            vcs_ref="main",
            exclude=excludes,
            overwrite=overwrite,
        )

    # Install template root components (like allauth -> templates/account/)
    for comp in root_components:
        dest_folder = TEMPLATE_ROOT_COMPONENTS[comp]
        component_excludes = [f"!{comp}"]
        excludes = ["*"] + component_excludes

        # Copy to a temp location first
        with tempfile.TemporaryDirectory() as tmpdir:
            copier.run_copy(
                src_path=COMPONENTS_REPO_URL,
                dst_path=Path(tmpdir),
                vcs_ref="main",
                exclude=excludes,
                overwrite=True,
            )

            # Move from temp/{comp}/* to templates/{dest_folder}/
            src_path = Path(tmpdir) / comp
            dest_path = Path("templates") / dest_folder

            if src_path.exists():
                if dest_path.exists() and overwrite:
                    shutil.rmtree(dest_path)
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_path, dest_path)


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

    with Status(f"Adding {component} component"):
        _install_component(components_to_install, overwrite)

    for comp in components_to_install:
        console.print(
            f"[bold green]:heavy_check_mark: Added {comp} component successfully![/]",
        )
