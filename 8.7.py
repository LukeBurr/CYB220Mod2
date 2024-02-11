def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

# Make three dictionaries representing different albums
album1 = make_album("Taylor Swift", "Fearless")
album2 = make_album("Ed Sheeran", "÷ (Divide)", 12)
album3 = make_album("Beyoncé", "Lemonade")

# Print each return value to show the album information
print(album1)
print(album2)
print(album3)
