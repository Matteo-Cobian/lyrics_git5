import requests
import json


def get_tabs_id(art, verbosity=True):

    """

     The function returns the guitar tabs of a song.

    :param artist: artist name
    :type artist: string
    :return: all the artist's songs information, the user have to pick the ID
    of the choosen song to insert in the provided link
    :rtype: string

    """

    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + art)

    data = json.loads(r.text)

    extended_output = 'To get the tabs insert the ID of the song after this ' \
        + 'link: http://www.songsterr.com/a/wa/song?id= \n\n' \
        + 'Here you can find IDs of every song of {},'.format(art) \
        + 'choose the one that you are searching for here: \n\n{}'.format(data)
    if verbosity:
        return extended_output
    else:
        return ('To get the tabs of the song insert the ID of the song in '
                'this link:  http://www.songsterr.com/a/wa/song?id=   ', data)
