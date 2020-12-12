## GIT5: SONG LYRICS and TABS FETCHER PROJECT 

Our project aims to grant users access to songs' lyrics and tabs through this simple tool that we created. 

### GETTING STARTED
The following guidelines will help final users to understand the whole project better and, of course, get a copy of our project and run it on their local machine for development and testing purposes.

### Repository structure

		music_package
						LICENSE.txt
						__init__.py
						lyrics.py
						tabs.py
						test			
									__init__.py
									test_module.py
		.gitignore
		README.rm
		database.db
		databmanager.py
		h_manager.py
		history.csv
		main.py



##### The package called ```music_package``` collects the following files:

- ```lyrics.py``` that query the [lyrics.ovh](https://lyricsovh.docs.apiary.io/#) website to fetch the lyrics of a song. It implements ```get_lyric( artist, title)``` function.

- ```tabs.py``` and [songsterr.com](http://www.songsterr.com/a/wa/song?id=) website to fetch the songs' tabs. It implemnts ```get_tabs_id( artist)``` function.

- ```__init__.py``` file is required to make Python treat directories containing the file as packages: ignore it!

- ```LICENSE.txt``` file contain the chosen license for GIT5 project.

##### The folder called ```test``` collects the following files:
- ```__init__.py``` file is required to make Python treat directories containing the file as packages: ignore it!
- ```test_module.py``` is a file which aim is to check if the code is working as it should. It contains three test cases to check the validity of different inputs.

##### Other files in the repository:

- ```.gitignore``` file specifies intentionally untracked files that git should ignore.

- ```database.db``` file stores all encripted usernames and encrypted passwords. Further information in the next section.

- ```databmanager``` file that allows to manage user database operations. It enable to create, check and remove accounts.

- ```h_manager``` file that allows to add user's researches into a csv file.

- ```history.csv``` csv file that contains records of all the user's tracks.

- ```main.py``` file that gathers all the function neatly and permits to execute the project aim.



### BEFORE STARTING: PREREQUISITES

1. Download of the repository from Git-hub [GIT5](https://github.com/Matteo-Cobian/lyrics_git5)

2. Check if all the needed libraries are installed.


:warning: The project requires the following modules to run:

 ```JSON``` , ```requests```, ```argparse```, ```sys``` , ```CSV```, ```os```, ```random```, ```hashlib``` modules. 

3. Use the command $ pip3 install libraryname to eventually install missing libraries.




	The system support a User Management System and so, you are going to need a valid username and password to login every time you execute the program.


### HANDS ON: POPULATE THE DB

4. Setup usernames and passwords, by executing databmanager.py from the command line.

		$ python databmanager.py -usr test -psw test -add/check/rm

	:warning: Only one operation at time is supported.

#### How to:

- ADD a new user

		$ python databmanager.py -usr test -psw test -add
			User [test] added to database!	
	

- CHECK an existing user's credentials

		$ python databmanager.py -usr test -psw test -check
			Credentials for user [test] are the correct ones!


- REMOVE an old user

		$ python databmanager.py -usr test -psw test -rm
			The user [{}] has been removed.


All the users and their passwords are saved in the database.db file in the repository. The file is now empty. As soon as users add new usernames and passwords, they will be stored in there. For security reasons, it will not be possible to read passwords straightforward: they are stored as digest computed with a salt plus hash repetition.



5. Execute the main file.

		$ python main.py "Artist" "Title" -usr *USERNAME* -psw *PASSWORD* -arguments*

:warning: Inputs must be written using double quotes " ".   

E.g.

```
$ Python main.py "Beatles" "Across the Universe"  -usr *USERNAME* -psw *PASSWORD* -v
The song Across the Universe is from the artist Beatles and the lyrics is:

Words are flowing out like 
Endless rain into a paper cup
They slither wildly as they slip away across the universe.
Pools of sorrow waves of joy
Are drifting through my opened mind
Possessing and caressing me.

.... **Lyrics** ....

 ('To get the tabs of the song insert the ID of the song in this link:  http://www.songsterr.com/a/wa/song?id=   ', [{'id': 57, 'type': 'Song', 'title': 'Blackbird', 'artist': {'id': 19, 'type': 'Artist', 'nameWithoutThePrefix': 'Beatles', 'useThePrefix': True, 'name': 'The Beatles'}, 'chordsPresent': True, 'tabTypes': ['PLAYER', 'TEXT_GUITAR_TAB', 'CHORDS']}, {'id': 2900, 'type': 'Song', 'title': "Octopus's Garden", 'artist': {'id': 19, 'type': 'Artist', 'nameWithoutThePrefix': 'Beatles', 'useThePrefix': True, 'name': 'The Beatles'}, 'chordsPresent': True, 'tabTypes': ['PLAYER', 'TEXT_GUITAR_TAB', 'CHORDS', 'TEXT_BASS_TAB']}, {'id': 59, 'type': 'Song', 'title': 'Girl', 'artist': {'id': 19, 'type': 'Artist', 'nameWithoutThePrefix': 'Beatles', 'useThePrefix': True, 'name': 'The Beatles'}, 'chordsPresent': True, 'tabTypes': ['PLAYER', 'TEXT_GUITAR_TAB', 'CHORDS', 'TEXT_BASS_TAB']}, {'id': 79, 'type': 'Song', 'title': 'Let It Be', 'artist': {'id': 19, 'type': 'Artist', 'nameWithoutThePrefix': 'Beatles', 'useThePrefix': True, 'name': 'The Beatles'}, 'chordsPresent': True, 'tabTypes': ['PLAYER', 'TEXT_GUITAR_TAB', 'CHORDS', 'TEXT_BASS_TAB']},

 .... **Other songs and tabs codes** ....
...
```



User can choose, ```title``` ( **Across the Universe** in the example) by the specified ```artist``` (**Beatles** in the example) to get the lyrics and tabs codes of all the song of the artist as output. 
In order to have acess to the tabs copy paste this link into your browsware http://www.songsterr.com/a/wa/song?id= and add the code that  is diplayed in the output.


E.g.


'id': 79, 'type': 'Song', 'title': 'Let It Be'


Copypasting the link + 79 (http://www.songsterr.com/a/wa/song?id=79) the user will see the tabs.


#### ARGUMENTS*

6. Chose the right arguments

In the command line the user must add some mandatory arguments to be able to use run the main script. 

**These are :** 

"Author" "Title"  : Insert them using double quotes " "

-usr : Insert username of the account

-psw: Insert password of the account

:warning: authentication is mandatory everytime users run the script.


**Moreover it is also possible to add some optional arguments:** 

'-v','--verbosity' : increase output verbosity

-h : show the help message

--version: show infos about the project.


QUI MANCA SOLO LA PARTE DEI PARAMETRI ED è CONCLUSO 




## DOCUMENTATION
Documentation is stored in the repository documentation. Please have a look to understand the functions of our modules better.
You should go in documentation/_build/html and select a file and it will open the documentation.

## CSV
In h_manager.py there is a code where the history of all the searches made in local is saved. This data is saved in a csv file created ad hoc, named history.csv.

## TESTING
Tests on parts of the code are provided here: ```music_package/test/``` .  
You can find the module ```test_module.py```. 
To run them, use:```python -m unittest -b music_package/tests/test_module.py```:

```
python -m unittest -b music_package/tests/test_module.py
test_correct_values(self) ... ok
test_empty_string(self) ... ok
test_wrong_values(self) ... ok


Ran 3 tests in 1.114s

OK
```

## SUPPORT

Do not hesitate if you need any support!

## AUTHORS AND ACKNOWLEDGMENT

- [Matteo Bianco](https://github.com/Matteo-Cobian)


- [Stefano Businaro](https://github.com/businer)


- [Francesco Di Vincenzo](https://github.com/divi999)


- [Federico Grego](https://github.com/Fede2302)


- [Virginia Massaccesi](https://github.com/Virginiaemme)


Also thanks to Prof. Pistellato and Prof. Maccari for their contribution.



## LICENSE
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)