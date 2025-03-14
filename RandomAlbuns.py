from pathlib import Path
import random
import tidalapi
session = tidalapi.Session()

try: 
    session.load_session_from_file(Path('../.authCache.txt'))
    if session.check_login() == False:
        raise Exception('no auth saved')
except Exception:
    session.login_oauth_simple()
    session.save_session_to_file(Path('../.authCache.txt'))

favorites = tidalapi.Favorites(session, session.user.id)

getMore = True
limit = 1000
offset = 0
albums = []
while getMore == True:
    pivotAlbums = favorites.albums(limit, offset)
    for i in range(len(pivotAlbums)):
        albums.append(pivotAlbums[i])
    offset += limit
    if len(pivotAlbums) == 0:
        getMore = False

print("total de Albuns: " + str(len(albums)))

tracks = 0

#tidalapi.Album.num_tracks
while tracks < 200:
    rnd = random.randrange(len(albums))
    rndAlbum = albums[rnd]
    tracks += rndAlbum.num_tracks
    print((str(rnd)) + " || " + rndAlbum.name + " || " + rndAlbum.artist.name+ " || ")
    print(str(tracks))


##for i in range(15):
##    rnd = random.randrange(len(albums))
##    rndAlbum = albums[rnd]
##    print((str(rnd)) + " " + rndAlbum.name + " " + rndAlbum.artist.name) 


