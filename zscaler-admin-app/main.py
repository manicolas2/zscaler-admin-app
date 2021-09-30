from typing import List, Optional

import typer

from utils import fetch_adminroles
from utils import fetch_adminrole_names
from utils import fetch_adminusers
from utils import fetch_adminuser_names
from utils import fetch_url_categories
from utils import fetch_url_category_names
from utils import create_custom_url_category


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
    
    if cmd == "create":
        pass


@app.command()
def urlcategory(
    cmd: str, 
    all: bool = False, 
    file: Optional[str] = None,
    name: Optional[str] = None,
    urls: Optional[List[str]] = None,
    dbcategorizedurls: Optional[List[str]] = None,
    description: Optional[str] = None,
):
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
        if file:
            message = create_custom_url_category(source_file_path=file)
            typer.echo(message)
        elif name and urls:
            typer.echo(name, urls)
            message = create_custom_url_category(
                configured_name=name,
                urls=urls,
                db_categorized_urls=dbcategorizedurls,
                description=description, 
            )
            typer.echo(message)
        else:
            name = typer.prompt("What's this URL Category Name?")
            urls = typer.prompt("Which URLs do you include? To input multiple, input with space.")
            urls = urls.split()
            description = typer.prompt("Please write a description of this URL Category.")
            message = create_custom_url_category(
               configured_name=name,
               urls=urls,
               db_categorized_urls=dbcategorizedurls,
               description=description, 
            )
            typer.echo(message)


if __name__ == "__main__":
    app()
