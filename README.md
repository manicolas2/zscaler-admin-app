## zscaler-admin-app


### What is this Repository
---
- This repository is CLI tools to manage Zscaler, especially ZIA.
- You could manage ZIA like
  - list and update Admin Role
  - list, create and update Admin User
  - list and update URL Category
  - create Custom URL Category
  - list, create and update URL Filtering Rule


### Prerequisites
---
- [poetry](https://python-poetry.org/docs/#installation)


### Instllation / Setup
---
1. To enter Virtual Environment, run `poetry shell`.
2. Install packages to run `poetry install`.
3. create ZIA credentials at `config/config.ini` in reference to `config/config.ini.sample`


### How to use
---
1. Admin Role
  - To show name of all admin role, `zia adminrole ls`.
  - To show all information, use `--all` option. (`zia adminrole ls --all`) 
 
2. Admin User
  - To show name and login name of all admin users, `zia adminuser ls`.
  - To show all information, use `--all` option. (`zia adminuser ls --all`) 

3. URL Category
  - To show configured names of URL Categories, `zia urlcategory ls`.
  - To show all information, use `--all` option. (`zia urlcategory ls --all`) 
