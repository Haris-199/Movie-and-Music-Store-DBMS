from django.shortcuts import render
from store.models import Artist, Song, Album, Franchise, Movie 


def home(request):
    query = request.GET.get('query')
    delete = request.GET.get('delete')

    insert_song_name = request.GET.get('song-name')
    insert_artist_name = request.GET.get('artist-name')
    insert_genre = request.GET.get('genre')
    insert_album = request.GET.get('album-name')
    insert_price = request.GET.get('price')

    a = {}
    if insert_artist_name:
        a = Artist.objects.filter(name=insert_artist_name)
        
    if insert_song_name and insert_artist_name and insert_genre and insert_price:
        s = Song.objects.create(name=insert_song_name, artist=a, genre=insert_genre, album=insert_album, price=insert_price)
        # s = Song.objects.create(song_name=insert_song_name, artist_name=a, genre=insert_genre, album_name=insert_album_name, price=insert_price)
        s.save()


    if delete:
        Song.objects.filter(song_name=delete).delete()

    context = { 
        'artists': Artist.objects.all(),
        'songs': Song.objects.all(),
        'albums': Album.objects.all(),
        'franchise': Franchise.objects.all(),
        'movie': Movie.objects.all(),
        'results': Song.objects.filter(song_name=query).first(),
    }
    
    return render(request, 'store/home.html', context)
