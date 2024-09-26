def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


while True:
    artist = input("Enter the artist's name (or 'quit' to exit): ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album's title: ")
    if title.lower() == 'quit':
        break

    album_info = make_album(artist, title)
    print(album_info)
