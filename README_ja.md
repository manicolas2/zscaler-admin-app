## zscaler-admin-app


### このリポジトリについて
---
- このリポジトリは、ZIA を CLI から操作するためのツールです。
- 以下の操作を CLI から実行できます。
  - 管理者ロールの一覧表示
  - 管理者ユーザの一覧表示/作成/更新
  - URLカテゴリの一覧表示/作成/更新
  - URLフィルタリングルールの一覧表示/作成/更新


### 事前準備
---
- [Python](https://www.python.org/)
- [poetry](https://python-poetry.org/docs/#installation)

- 実行コマンド
  1. ローカルPCでコードの準備 
  2. 仮想環境に移行
    `poetry shell`.
  3. 依存するライブラリのインストール
    `poetry install`.
  4. 対象の ZIA クレデンシャル情報を `config/config.ini` にセットアップ
     以下は設定例
    ```
    [tenant name]
    USERNAME=user@zscaler.net
    PASSWORD=P@ssword
    HOSTNAME=zscaler.net
    APIKEY= xxx
    ```


### 使用方法
---
1. 管理者ロール
  - 管理者ロールの一覧表示
    - `zia adminrole ls`.
  - オプション 
    - `--all` (`zia adminrole ls --all`) -> 詳細情報の表示
    - `--tenant` (`zia adminrole ls --tenant=<tenant_name>`) -> 指定テナントの情報表示
 
2. 管理者ユーザ
  - 管理者ユーザの一覧表示
    `zia adminuser ls`.
  - 管理者ユーザの作成
    `zia adminuser create --file=sample/sample_adminuser.json --tenant=<tenant>`.
  - オプション
    - `--all` (`zia adminuser ls --all`) -> 詳細情報の表示
    - `--tenant` (`zia adminuser ls --tenant=<tenant_name>`) -> 指定テナントの情報表示
  - 管理者ユーザの更新
    - To be...

3. URLカテゴリ
  - URLカテゴリの一覧表示
    - `zia urlcategory ls`.
- URLカテゴリの作成
    - `zia urlcategory create --file=sample/sample_adminuser.json --tenant=<tenant>`.
- オプション
    - `--all` (`zia adminuser ls --all`) -> 詳細情報の表示
    - `--tenant` (`zia adminuser ls --tenant=<tenant_name>`) -> 指定テナントの情報表示

4. URLフィルタリングルール
  - URLカテゴリの一覧表示
    - `zia urlfilter ls`
  - URLカテゴリの作成
    - `zia urlfilter create --file=sample/sample_adminuser.json --tenant=<tenant>`.

### Support Feature

|  TH  |  TH  |
| ---- | ---- |
|  TD  |  TD  |
