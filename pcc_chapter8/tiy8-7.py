# PCC Try It Yourself 8-7. Album.

def make_album(artist, album_title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {'artist': artist, 'album title': album_title}
    if tracks:
        album['track number'] = tracks

    return album

album_info = make_album('linkin park', 'hybrid theory', 12)
print(album_info)

album_info = make_album('tool', '10,000 days')
print(album_info)

album_info = make_album('system of a down', 'steal this album', 13)
print(album_info)

while True:
    print("\nPlease enter your album information:")
    print("(enter 'q' at any time to quit)")

    artist_name = input("\nArtist name: ")
    if artist_name == 'q':
        break

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    album_info = make_album(artist_name, album_name)
    print(album_info)