import typer

app = typer.Typer(no_args_is_help=True)


@app.command(name="add")
def add():
    """
    Add a new component to your project
    """
    typer.echo("Adding a new component...")
    typer.echo("Component added successfully!")
