import argparse


def adminUser():
    parser = argparse.ArgumentParser(description="Operate adminUser controls.")
    parser.add_argument(
        "cmd",
        help="Commands for adminuser operations like show users, update, create new users",
        type=str,
    )
    parser.add_argument(
        "--tenant", 
        help="Specify target tenant",
        type=str,
    )
    # parser.add_argument(
    #     '',
    #     required=True,
    #     metavar='FUNC',
    #     type=int,
    #     nargs='+',
    #     help='an integer for the accumulator'
    # )
    # parser.add_argument(
    #     '--sum',
    #     dest='accumulate',
    #     action='store_const',
    #     const=sum,
    #     default=max,
    #     help='sum the integers (default: find the max)'
    # )
    args = parser.parse_args()
    if args.cmd == "ls":
        print(
            '{"id":45593290,"loginName":"yuta.kawamura@zscaler.net","userName":"Yuta Kawamura","email":"yuta.kawamura@zscaler.net","role":{"id":41577,"name":"Super Admin","isNameL10nTag":true,"extensions":{"adminRank":"0","roleType":"EXEC_INSIGHT_AND_ORG_ADMIN"}},"adminScopescopeGroupMemberEntities":[],"adminScopeType":"ORGANIZATION","adminScopeScopeEntities":[],"isPasswordLoginAllowed":true,"pwdLastModifiedTime":1622193781,"name":"Yuta Kawamura"}'
        )
    if args.tenant:
        print(f"Tenant: {args.tenant}")
