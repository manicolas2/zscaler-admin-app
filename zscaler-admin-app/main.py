import typer

from utils import fetch_adminroles
from utils import fetch_adminrole_names
from utils import fetch_adminusers
from utils import fetch_adminuser_names
from utils import fetch_url_categories
from utils import fetch_url_category_names


app = typer.Typer()


@app.command()
def adminrole(cmd: str, all: bool = False):
    if cmd is None:
        typer.echo("Please set correct cmd after `adminrole`")
    
    if cmd == "ls":
        if all:
            for role in fetch_adminroles():
                typer.echo(role)
        else:
            for role in fetch_adminrole_names():
                typer.echo(role)


@app.command()
def adminuser(cmd: str, all: bool = False):
    if cmd is None:
        typer.echo("Please set correct cmd after `adminuser`")

    if cmd == "ls":
        if all:
            for user in fetch_adminusers():
                typer.echo(user)
        else:
            for user in fetch_adminuser_names():
                typer.echo(user)


@app.command()
def urlcategory(cmd: str, all: bool = False, policy_file: str = None):
    if cmd is None:
        typer.echo("Please set correct cmd after `urlcategory`")

    if cmd == "ls":
        if all:
            for result in fetch_url_categories():
                typer.echo(result)
        else:
            for result in fetch_url_category_names():
                typer.echo(result)

    if cmd == "create":
        if policy_file:
            for result in fetch_url_categories():
                typer.echo(result)
        else:
            typer.echo("Please set correct opotion with `--policy_file`")



if __name__ == "__main__":
    app()
