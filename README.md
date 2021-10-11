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
1. Cloen this repository, run `git clone https://github.com/yuta519/zscaler-admin-app.git`.
2. To enter Virtual Environment, run `poetry shell`.
3. Install packages to run `poetry install`.
4. Write the ZIA credential infolmation at `config/config.ini` like
  ```
  [credential]
  USERNAME=user@zscaler.net
  PASSWORD=P@ssword
  HOSTNAME=zscaler.net
  APIKEY= xxx
  ```


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

4. URL Filtering Rules 
  - To show configured names of URL Filtering Rules, `zia urlfilter ls`.
  - To show all information, use `--all` option. (`zia urlfilter ls --all`) 

### Support Feature

|  TH  |  TH  |
| ---- | ---- |
|  TD  |  TD  |
