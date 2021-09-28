import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


@app.command()
def adminuser(cmd: str):
    sample_result = """
        {
            "id":45593290,
            "loginName":"yuta.kawamura@zscaler.net",
            "userName":"Yuta Kawamura",
            "email":"yuta.kawamura@zscaler.net",
            "role":{"id":41577,"name":"Super Admin",
            "isNameL10nTag":true,
            "extensions":{
                "adminRank":"0",
                "roleType":"EXEC_INSIGHT_AND_ORG_ADMIN"
            }
        },
        "adminScopescopeGroupMemberEntities":[],
        "adminScopeType":"ORGANIZATION",
        "adminScopeScopeEntities":[],
        "isPasswordLoginAllowed":true,
        "pwdLastModifiedTime":1622193781,
        "name":"Yuta Kawamura"
    }
    """
    if cmd == "ls":
        typer.echo(sample_result)
    else:
        typer.echo("Please set correct cmd after `adminuser`")


if __name__ == "__main__":
    app()
