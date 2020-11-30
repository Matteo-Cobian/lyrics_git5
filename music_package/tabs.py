def get_tabs_id(artist):

""" 

The function returns the guitar tabs of a song.

"""

    r = requests.get('http://www.songsterr.com/a/ra/songs.json?pattern=' + artist)

    my_dict = r.json()

    return (my_dict, 'You will find the tabs of the song by googling http://www.songsterr.com/a/wa/song?id= and add the id of the song you want' )