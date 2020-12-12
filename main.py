from music_package import lyrics as ly
from music_package import tabs as ta
import argparse as arg
import os
import databmanager
import sys
import h_manager as hm
import csv
import pandas as pd


def argparse():

    '''
    The inputs are collected and parsed,
    then the results will be organized in arrays to be inserted in the URL.
    Arguments:
    
        ["-artist"]: insert the name of the artist
        ["-title"]: insert the title of the song you are looking for
        ["-v"]: add verbosity
        ["-usr"]: insert user name
        ["-psw"]: insert user password

    '''

    parser = arg.ArgumentParser()
    parser.add_argument(
        "artist", type = str,
        help="add artist between double quotes")
    parser.add_argument(
        "title", type = str,
        help="add title between double quotes")
    parser.add_argument(
        '-v', '--verbosity',
        help='increase output verbosity',
        action='store_true')
    parser.add_argument(
        '-usr',
        help="Write your username here",
        required=True)
    parser.add_argument('-psw', help="Write your password here",
                        required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":

    '''
    Execute code only if the file was run directly.
    If the user has correctly logged in, run the program.

    :param song_lyrics: lyrics of the song
    :type song_lyrics: string
    :param song_tabs: collection of all the songs of the artist with the
    associated information, you need the ID
    :type song_tabs: list
    :return: the lyrics of the song and the list of the artist's songs where
    to search the needed ID for getting the tabs
    :rtype: string, list

    '''

    databmanager.open_and_create('database.db')
    args = argparse()

    if databmanager.check_user(args.usr, args.psw):
        df = pd.read_csv('history.csv')
        # Creating a dictionary
        dic = {'artist': args.artist, 'song': args.title, 'username': args.usr}
        # Creating the keys of the dictionary
        fieldn = ['artist', 'song', 'username']
        # Appending the file to our csv
        hm.append_dict_as_row('history.csv', dic, fieldn)
        song_lyrics = ly.get_lyric(args.artist, args.title, args.verbosity)
        song_tabs = ta.get_tabs_id(args.artist, args.verbosity)
        print(song_lyrics, '\n\n', song_tabs)

    else:
        print('''Sorry, wrong username password selected!
        You may wanna register a new account through databmanager app.
        ''')