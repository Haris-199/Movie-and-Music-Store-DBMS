from django.urls import path
from .views import (home, ArtistListView, ArtistSearchListView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView, SongListView, SongSearchListView, SongCreateView, SongUpdateView, SongDeleteView, AlbumListView, AlbumSearchListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView, FranchiseListView, FranchiseSearchListView, FranchiseCreateView, FranchiseUpdateView, FranchiseDeleteView, MovieListView, MovieSearchListView, MovieCreateView, MovieUpdateView, MovieDeleteView)


# These are the routes a user may visit
urlpatterns = [
    path('', home, name='store-home'),
    
    path('artist/', ArtistListView.as_view(), name='store-artist'),
    path('artist/search/', ArtistSearchListView.as_view(), name='artist-search'),
    path('artist/create', ArtistCreateView.as_view(), name='artist-create'),
    path('artist/<pk>/update', ArtistUpdateView.as_view(), name='artist-update'),
    path('artist/<pk>/delete', ArtistDeleteView.as_view(), name='artist-delete'),

    path('song/', SongListView.as_view(), name='store-song'),
    path('song/search/', SongSearchListView.as_view(), name='song-search'),
    path('song/create', SongCreateView.as_view(), name='song-create'),
    path('song/<pk>/update', SongUpdateView.as_view(), name='song-update'),
    path('song/<pk>/delete', SongDeleteView.as_view(), name='song-delete'),
    
    path('album/', AlbumListView.as_view(), name='store-album'),
    path('album/search/', AlbumSearchListView.as_view(), name='album-search'),
    path('album/create', AlbumCreateView.as_view(), name='album-create'),
    path('album/<pk>/update', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<pk>/delete', AlbumDeleteView.as_view(), name='album-delete'),

    path('franchise/', FranchiseListView.as_view(), name='store-franchise'),
    path('franchise/search/', FranchiseSearchListView.as_view(), name='franchise-search'),
    path('franchise/create', FranchiseCreateView.as_view(), name='franchise-create'),
    path('franchise/<pk>/update', FranchiseUpdateView.as_view(), name='franchise-update'),
    path('franchise/<pk>/delete', FranchiseDeleteView.as_view(), name='franchise-delete'),

    path('movie/', MovieListView.as_view(), name='store-movie'),
    path('movie/search/', MovieSearchListView.as_view(), name='movie-search'),
    path('movie/create', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<pk>/update', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<pk>/delete', MovieDeleteView.as_view(), name='movie-delete'),
]
