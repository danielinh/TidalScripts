from pathlib import Path
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
tot = 0

while getMore == True:
    pivotAlbums = favorites.albums(limit, offset)
    for i in range(len(pivotAlbums)):
        if (not pivotAlbums[i].available):
            print (str(pivotAlbums[i].id)+ " "+ pivotAlbums[i].name + "  " +pivotAlbums[i].artist.name)
            #favorites.remove_album(pivotAlbums[i].id)
            tot+=1
    offset += limit
    if len(pivotAlbums) == 0:
        getMore = False

print("Total Indisponivel : "+ str(tot))