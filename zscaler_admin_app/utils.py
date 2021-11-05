import json
from typing import Any, Optional
from typing import Dict
from typing import List

from zscaler_python_sdk import admin
from zscaler_python_sdk import url_categories
from zscaler_python_sdk import url_filtering_rules
from zscaler_python_sdk import users

from zscaler_python_sdk import utils


def fetch_adminroles(tenant: str = None) -> List[Dict[Any, Any]]:
    adminroles = admin.fetch_adminroles(tenant=tenant)
    return adminroles


def fetch_adminrole_names(tenant: Optional[str] = None) -> List[str]:
    adminroles = admin.fetch_adminroles(tenant=tenant)
    if tenant is not None:
        role_names = [role["name"] for role in adminroles[tenant]]
        return {tenant: role_names}
    else:
        all_tenant_results: Dict[str, List[str]] = {}
        for tenant_name in adminroles.keys():
            all_tenant_results[tenant_name] = [
                role["name"] for role in adminroles[tenant_name]
            ]
        return all_tenant_results


def fetch_adminusers(tenant: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
    adminusers = admin.fetch_adminusers(tenant=tenant)
    return adminusers


def fetch_adminuser_names(tenant: Optional[str] = None) -> Dict[str, Dict[str, Any]]:
    adminusers = admin.fetch_adminusers(tenant=tenant)
    for tenant_name in adminusers.keys():
        adminusers[tenant_name] = [
            f"{user['userName']} ({user['loginName']})"
            for user in adminusers[tenant_name]
        ]
    return adminusers


def create_new_adminuser(
    tenant: str,
    source_file_path: Optional[str] = None,
    login_name: Optional[str] = None,
    user_name: Optional[List[str]] = None,
    email: Optional[List[str]] = None,
    password: Optional[str] = None,
    role_name: Optional[str] = None,
) -> Dict[str, Any]:
    if source_file_path is not None:
        with open(source_file_path) as file:
            parameters = json.load(file)
            login_name = parameters["loginName"]
            user_name = parameters["userName"]
            email = parameters["email"]
            password = parameters["password"]
            role_name = parameters["role"]

    message: str = admin.create_adminuser(
        loginName=login_name,
        userName=user_name,
        email=email,
        password=password,
        rolename=role_name,
        tenant=tenant,
    )
    return message


def fetch_users(tenant: Optional[str]):
    user_list: Dict[str, Any] = users.fetch_users(tenant=tenant)
    return user_list


def fetch_user_summary(tenant: Optional[str]):
    users_summary: Dict[str, Any] = users.fetch_users(tenant=tenant)
    user_summary: List[Dict[str, str]] = []
    for tenant_name in users_summary.keys():
        for user in users_summary[tenant_name]:
            username: str = user["name"]
            email: str = user["email"]
            groups: List[str] = [group["name"] for group in user["groups"]]
            department: str = (
                user["department"]["name"] if "department" in user.keys() else None
            )
            user_summary.append(
                f"{username} (Mail: {email}, Group: {groups}, Department: {department})"
            )
        users_summary[tenant_name] = user_summary
    return users_summary


def fetch_departments(tenant: Optional[str]):
    departments: Dict[str, Any] = users.fetch_departments(tenant=tenant)
    return departments


def fetch_department_summary(tenant: Optional[str]):
    departments: Dict[str, Any] = users.fetch_departments(tenant=tenant)
    for tenant_name in departments.keys():
        dpt_name: List[str] = [dpt["name"] for dpt in departments[tenant_name]]
        departments[tenant_name] = dpt_name
    return departments


def fetch_groups(tenant: Optional[str]):
    groups: Dict[str, Any] = users.fetch_groups(tenant=tenant)
    return groups


def fetch_group_summary(tenant: Optional[str]):
    groups: Dict[str, Any] = users.fetch_groups(tenant=tenant)
    for tenant_name in groups.keys():
        group: List[str] = [group["name"] for group in groups[tenant_name]]
        groups[tenant_name] = group
    return groups


def fetch_url_categories(tenant: Optional[str] = None) -> Dict[Any, Any]:
    response: List[Dict[Any, Any]] = url_categories.fetch_url_categories(tenant=tenant)
    return response


def fetch_url_category_names(tenant: Optional[str] = None) -> Dict[str, List[str]]:
    response: Dict[str, Any] = url_categories.fetch_url_categories(tenant=tenant)
    for tenant_name in response.keys():
        category_list: List[str] = []
        for category in response[tenant_name]:
            if "configuredName" not in category.keys():
                category_list.append(category["id"])
            else:
                category_list.append(f"{category['id']} ({category['configuredName']})")
        response[tenant_name] = category_list
    return response


def create_custom_url_category(
    tenant: str,
    source_file_path: Optional[str] = None,
    configured_name: Optional[str] = None,
    urls: Optional[List[str]] = None,
    db_categorized_urls: Optional[List[str]] = None,
    description: Optional[str] = None,
) -> str:
    if source_file_path:
        with open(source_file_path) as file:
            parameters = json.load(file)
            configured_name = parameters["configuredName"]
            urls = parameters["urls"]
            db_categorized_urls = parameters["dbCategorizedUrls"]
            description = parameters["description"]

    message = url_categories.create_custom_url_category(
        configured_name,
        urls,
        db_categorized_urls,
        description,
        tenant=tenant,
    )
    return message


def fetch_urlfiltering_rule_names(tenant: str) -> Dict[str, List[str]]:
    url_filter_rules = url_filtering_rules.fetch_all_url_filering_rules(tenant=tenant)
    for tenant_name in url_filter_rules.keys():
        names_of_urlfilter_rules = [
            (
                f"{rule['name']} (Order: {rule['order']}, Action: {rule['action']}, "
                f"Status: {rule['state']})"
            )
            for rule in url_filter_rules[tenant_name]
        ]
        url_filter_rules[tenant_name] = names_of_urlfilter_rules
    return url_filter_rules


def fetch_urlfiltering_rule_details(tenant: str) -> List[str]:
    url_filter_rules = url_filtering_rules.fetch_all_url_filering_rules(tenant=tenant)
    return url_filter_rules


def create_urlfiltering_rule(
    source_file_path: str,
    tenant: str,
) -> Dict[str, Any]:
    with open(source_file_path) as file:
        parameters = json.load(file)
        rule_name = parameters["name"]
        order = parameters["order"]
        protocols = parameters["protocols"]
        locations = parameters["locations"]
        groups = parameters["groups"]
        departments = parameters["departments"]
        users = parameters["users"]
        url_categories = utils.translate_category_from_name_to_id(
            parameters["urlCategories"], tenant
        )
        state = parameters["state"]
        rank = parameters["rank"]
        action = parameters["action"]

    message: Dict[str, Any] = url_filtering_rules.create_url_filering_rules(
        name=rule_name,
        order=order,
        protocols=protocols,
        locations=locations,
        groups=groups,
        departments=departments,
        users=users,
        url_categories=url_categories,
        state=state,
        rank=rank,
        action=action,
        tenant=tenant,
    )
    return message
