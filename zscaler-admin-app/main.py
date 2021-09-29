import typer
from zscaler_python_sdk import url_categories

# from zscaler_python_sdk import url_categories

app = typer.Typer()


@app.command()
def adminuser(cmd: str):
    # if cmd is None:
    #     typer.echo("Please set correct cmd after `adminuser`")

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


@app.command()
def urlcategory(cmd: str):
    if cmd is None:
        typer.echo("Please set correct cmd after `adminuser`")

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



if __name__ == "__main__":
    
    print(url_categories.fetch_url_categories())
    app()
