#!/usr/bin/env python3

import pwd
import argparse
from pprint import pprint
from user import User


def list_users(verbose, sid=500):
    users = pwd.getpwall()
    users.sort(key=lambda user: user[2])
    sys_users = []
    gen_users = []
    for user in users:
        if user[2] <= sid:
            sys_users.append(User(*user))
        else:
            gen_users.append(User(*user))
    if verbose:
        print('You have following System Users on your system:')
        print('name, uid, gid, fullname, home, shell')
        print('======================================')
    for user in sys_users:
        print(user)

    if verbose:
        print('\nYou have following General Users on your system:')
        print('name, uid, gid, fullname, home, shell')
        print('======================================')
    for user in gen_users:
        print(user)


parser = argparse.ArgumentParser(prog='um',
    description='A more informative and modern user manager for Linux/Unix')

group = parser.add_mutually_exclusive_group()
group.add_argument('-l', '--list', dest='action', action='store_const', 
                   const='list', help='list the users on the system')

parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase output verbosity')

args = parser.parse_args()

if args.action is 'list':
    list_users(args.verbose)
