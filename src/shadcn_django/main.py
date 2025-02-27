import typer

from .add import app as add_app
from .initialize import app as init_app
from .list import app as list_app

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.callback()
def callback():
    """
    shadcn/ui for your Django projects
    """


app.add_typer(init_app)
app.add_typer(add_app)
app.add_typer(list_app)
