#! /usr/bin/env python3
''' databmanager.py is a module that allows to manage user database operations.
It will enable to: (1) create a new account with username and password,
(2) check if the provided credentials are in the database, and
(3) delete an account from the database
The module can be called directly or through the main file in order to manage
the database, check if the user is registered or not and allow the access.
'''

import sqlite3
import hashlib
import random
import os
from argparse import ArgumentParser

conn = None
cursor = None


def open_and_create(database):

    """ This function allows to create a new database or to connect to an
    existing one.
    :param database: path to database
    :type database: string
    """
    global conn
    global cursor
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        conn.commit()
    except sqlite3.OperationalError:
        cursor.execute('''CREATE TABLE users
                      (username CHAR(256) NOT NULL,
                       digest CHAR(256) NOT NULL,
                       salt SMALL INT NOT NULL,
                       PRIMARY KEY (username))''')


def parse_args():
    '''Command line option and argument parsing.
    The function uses argparse to write user-friendly command-line interfaces.
    The argparse module also automatically generates help and usage messages
    and issues errors when users give the program invalid arguments.
    Arguments:
        ["-usr"] (required): Insert username of the account
        ["-psw"] (required): Insert password of the account
        ["-add"]: add a user
        ["-rm"]: remove a user
        ["-check"]: check a user
        ["--version"] (optional): show infos about the project

    :return: user shell inputs arguments
    :rtype: namespace
    '''

    parser = ArgumentParser(
        description="Managing of the users database",
        usage="%(prog)s [options]",
        epilog="Backend SQLite3")
    parser.add_argument(
        '-usr',
        help="Write your username here",
        required=True)
    parser.add_argument(
        '-psw',
        help="Write your password here",
        required=True)
    parser.add_argument(
        '-rm',
        help="Remove a user from the database",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        '-add',
        help="add a username",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        '-check',
        help="check if credentials are present in the database",
        action="store_true",
        default=False,
        required=False)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s v1.0, Nov 2020 by NOISIAMOVELOCITAsoftware©")

    arguments = parser.parse_args()
    return arguments


def new_user(user, passw):
    """ This function allows to register a new user.
    The SHA256, of salt plus password, is computed to obtain the digest.
    In this way passwords can be stored in encrypted version to provide
    security.
    :param user: user username
    :type user: string
    :param passw: user password
    :type passw: string
    """
    global conn
    global cursor
    sale = str(random.randint(1, 10000))
    digest = sale + passw
    for i in range(100000):
        digest = hashlib.sha256(passw.encode('utf-8')).hexdigest()
    row = cursor.execute("SELECT * FROM users WHERE username=?", (user,))
    results = row.fetchall()
    if results:
        print("Sorry, username [{}] is already in use. Please, retry!"
              .format(user))
        quit()
    else:
        cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                       (user, digest, sale))
        conn.commit()
        print("User [{}] added to database!".format(user))


def check_user(user, passw):
    """ Check if credentials are correct.
    If the user exists the SHA256 is computed. Than, if the digest of the
    password provided by the user corresponds to the digest computed above,
    the user is authenticated and allowed to use functionalities.
    :param user: user username
    :type user: string
    :param passw: user password
    :type passw: string
    :return: `True` if log in was successful, `False` otherwise
    :rtype: bool
    """
    global conn
    global cursor
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM users WHERE username=?",
                          (user,))
    results = rows.fetchall()
    conn.commit()
    if results == []:
        print('''
              Sorry, the password is incorrect.
              You may wanna register a new account through databmanager app.
              ''')
        quit()
    password = str(results[0][2]) + passw
    digest = hashlib.sha256(passw.encode('utf-8')).hexdigest()
    if digest == results[0][1].lower():
        return True
    else:
        return False


def remove_user(user, psw):
    """ Remove a user.
    :param user: user username
    :type user: string
    :param passw: user password
    :type passw: string
    """
    global conn
    global cursor
    if check_user(user, psw):
        cursor.execute("DELETE FROM users WHERE username = ?", (user,))
        conn.commit()
        print("The user [{}] has been removed.".format(args.usr))
    else:
        print("Sorry, the password provided is not correct. Try again.")


if __name__ == "__main__":
    ''' Execute code only if the file was run directly.
    '''
    open_and_create('database.db')
    args = parse_args()
    bool1 = args.add and args.rm
    bool2 = args.add and args.check
    bool3 = args.rm and args.check
    if bool1 or bool2 or bool3:
        print("ATTENTION!! Can't execute both operations at the same time!")
        quit()
    if args.add:
        if args.usr is None or args.psw is None:
            print("Sorry, both username and password are required!")
        else:
            new_user(args.usr, args.psw)
    elif args.rm:
        remove_user(args.usr, args.psw)
    elif args.check:
        if check_user(args.usr, args.psw):
            print("Credentials for user [{}] are the correct ones!"
                  .format(args.usr))
        else:
            print("Sorry, the password selected is wrong or invalid.")
    else:
        print("Please select one operation [-add], [-rm] or [-check]!")
        conn.close()
