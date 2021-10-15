from typing import Any
from typing import Dict
from typing import List
from typing import Optional

import typer

from zscaler_admin_app.utils import fetch_adminroles
from zscaler_admin_app.utils import fetch_adminrole_names
from zscaler_admin_app.utils import fetch_adminusers
from zscaler_admin_app.utils import fetch_adminuser_names
from zscaler_admin_app.utils import create_new_adminuser
from zscaler_admin_app.utils import fetch_url_categories
from zscaler_admin_app.utils import fetch_url_category_names
from zscaler_admin_app.utils import create_custom_url_category
from zscaler_admin_app.utils import fetch_urlfiltering_rule_names
from zscaler_admin_app.utils import fetch_urlfiltering_rule_details


app = typer.Typer()


@app.command()
def adminrole(
    cmd: str,
    all: bool = False,
    tenant: Optional[str] = None,
):
    if cmd == "ls":
        if all:
            response: Dict[str, List[Any]] = fetch_adminroles(tenant=tenant)
            if tenant is not None:
                typer.echo(f"# Tenant: {tenant}")
                for role in response[tenant]:
                    typer.echo(role)
            else:
                for tenant_name in response.keys():
                    typer.echo(f"# Tenant: {tenant_name}")
                    for role in response[tenant_name]:
                        typer.echo(role)
        else:
            response: Dict[str, List[str]] = fetch_adminrole_names(tenant=tenant)
            if tenant is not None:
                typer.echo(f"# Tenant: {tenant}")
                for role in response[tenant]:
                    typer.echo(f"  - {role}")
            else:
                for tenant_name in response.keys():
                    typer.echo(f"# Tenant: {tenant_name}")
                    for role in response[tenant_name]:
                        typer.echo(f"  - {role}")


@app.command()
def adminuser(
    cmd: str,
    all: bool = False,
    file: Optional[str] = None,
    loginname: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
    role: Optional[str] = None,
    tenant: Optional[str] = None,
):
    if cmd == "ls":
        if all:
            response: Dict[str, Dict[str, Any]] = fetch_adminusers(tenant=tenant)
            if tenant is not None:
                typer.echo(f"# Tenant: {tenant}")
                for adminuser in response[tenant]:
                    typer.echo(adminuser)
            else:
                for tenant_name in response.keys():
                    typer.echo(f"# Tenant: {tenant_name}")
                    for user in response[tenant_name]:
                        typer.echo(f"  - {user}")
        else:
            response: Dict[str, Any] = fetch_adminuser_names(tenant=tenant)
            if tenant is not None:
                typer.echo(f"# Tenant: {tenant}")
                for user in response[tenant]:
                    typer.echo(f"  - {user}")
            else:
                for tenant_name in response.keys():
                    typer.echo(f"# Tenant: {tenant_name}")
                    for user in response[tenant_name]:
                        typer.echo(f"  - {user}")
    if cmd == "create":
        if tenant is None:
            typer.echo("Please set `--tenant` to create adminuser")
            return
        if file is not None:
            message: str = create_new_adminuser(source_file_path=file, tenant=tenant)
            typer.echo(message)
        elif loginname is username is email is password is role is not None:
            message: str = create_new_adminuser(
                login_name=loginname,
                user_name=username,
                email=email,
                password=password,
                role_name=role,
                tenant=tenant,
            )
            typer.echo(message)
        # else:
        # TODO: create prompt
        # login_name = typer.prompt("What's this URL Category Name?")


@app.command()
def urlcategory(
    cmd: str,
    all: bool = False,
    tenant: Optional[str] = None,
    file: Optional[str] = None,
    name: Optional[str] = None,
    urls: Optional[List[str]] = None,
    dbcategorizedurls: Optional[List[str]] = None,
    description: Optional[str] = None,
):
    if cmd == "ls":
        if all:
            response: Dict[str, Any] = fetch_url_categories(tenant=tenant)
            for tenant_name in response.keys():
                typer.echo(f"# Tenant: {tenant_name}")
                for urlcategory in response[tenant_name]:
                    typer.echo(urlcategory)
        else:
            response: Dict[str, Any] = fetch_url_category_names(tenant=tenant)
            for tenant_name in response.keys():
                typer.echo(f"# Tenant: {tenant_name}")
                for urlcategory in response[tenant_name]:
                    typer.echo(f"  - {urlcategory}")

    if cmd == "create":
        if file:
            message = create_custom_url_category(source_file_path=file, tenant=tenant)
            typer.echo(message)
        elif name and urls:
            typer.echo(name, urls)
            message = create_custom_url_category(
                configured_name=name,
                urls=urls,
                db_categorized_urls=dbcategorizedurls,
                description=description,
                tenant=tenant,
            )
            typer.echo(message)
        else:
            name = typer.prompt("What's this URL Category Name?")
            urls = typer.prompt("Which URL do you include? For multiple,include space.")
            urls = urls.split()
            description = typer.prompt(
                "Please write a description of this URL Category."
            )
            message = create_custom_url_category(
                configured_name=name,
                urls=urls,
                db_categorized_urls=dbcategorizedurls,
                description=description,
                tenant=tenant,
            )
            typer.echo(message)


@app.command()
def urlfilter(
    cmd: str,
    all: bool = False,
    file: Optional[str] = None,
    tenant: Optional[str] = None,
):
    if cmd == "ls":
        if all:
            response: Dict[str, Any] = fetch_urlfiltering_rule_details(tenant=tenant)
            for tenant_name in response.keys():
                typer.echo(f"# Tenant: {tenant_name}")
                for rule in response[tenant_name]:
                    typer.echo(rule)
        else:
            response: Dict[str, Any] = fetch_urlfiltering_rule_names(tenant=tenant)
            for tenant_name in response.keys():
                typer.echo(f"# Tenant: {tenant_name}")
                for rule in response[tenant_name]:
                    typer.echo(f"  - {rule}")

    if cmd == "create":
        if file:
            pass
        else:
            pass
