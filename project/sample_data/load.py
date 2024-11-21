import json
from store.models import Artist, Song, Album, Franchise, Movie

def main():
    with open('arists.json') as f:
        artists_json = json.load(f)
    for a in artists_json:
        artist = Artist(artist_name=a['artist_name'], genres=a['genres'], listeners=a['listeners'])
        artist.save()

    with open('songs.json') as f:
        songs_json = json.load(f)
    for s in songs_json:
        song = Song(product_id=s['product_id'], song_name=a['song_name'], artist_name = s['artist_name'], genre=s['genre'], album_name=s['album_name'], price=s['price'])
        song.save()

    with open('albums.json') as f:
        albums_json = json.load(f)
    for a in albums_json:
        album = Album(product_id=a['product_id'], artist_name=a['artist_name'], album_name=a['album_name'], price=a['price'])
        album.save()

    with open('franchises.json') as f:
        franchises_json = json.load(f)
    for f in franchises_json:
        franchise = Franchise(product_id=f['product_id'], franchise_name=f['franchise_name'], price=f['price'])
        franchise.save()

    with open('movies.json') as f:
        movies_json = json.load(f)
    for m in movies_json:
        movie = Movie(product_id=m['product_id'], movie_name=m['movie_name'], genre=m['genre'], director=m['director'], actors=m['actors'], price=m['price'], franchise_name=m['franchise_name'])
        movie.save()

if __name__ == "__main__":
    main()
