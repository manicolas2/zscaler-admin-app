from typing import Any
from typing import Dict
from typing import List

from zscaler_python_sdk import admin
from zscaler_python_sdk import url_categories


def fetch_adminroles() -> List[Dict[Any, Any]]:
    adminroles = admin.fetch_adminroles()
    return adminroles

def fetch_adminrole_names() -> List[str]:
    adminroles = admin.fetch_adminroles()
    role_names = [role["name"] for role in adminroles]
    return role_names

def fetch_adminusers():
    adminusers = admin.fetch_adminusers()
    return adminusers

def fetch_adminuser_names() -> List[str]:
    adminusers = admin.fetch_adminusers()
    response: List[str] = [f"{user['userName']} ({user['loginName']})" for user in adminusers]
    return response

def fetch_url_categories() -> List[ List[Dict[Any, Any]]]:
    response: List[Dict[Any, Any]] = url_categories.fetch_url_categories()
    return response

def fetch_url_category_names() -> List[str]:
    categories: List[Dict[Any, Any]] = url_categories.fetch_url_categories()
    response: List[str] = []
    for category in categories:
        if "configuredName" not in category.keys():
            response.append(category["id"])
        else:
            response.append(f"{category['id']} ({category['configuredName']})")
    return response