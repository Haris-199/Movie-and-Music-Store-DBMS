from django.urls import path
from .views import (home, SongListView, SongCreateView, SongUpdateView, SongDeleteView, AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView)


urlpatterns = [
    path('', home, name='store-home'),

    path('song/', SongListView.as_view(), name='store-song'),
    path('song/create', SongCreateView.as_view(), name='song-create'),
    path('song/<pk>/update', SongUpdateView.as_view(), name='song-update'),
    path('song/<pk>/delete', SongDeleteView.as_view(), name='song-delete'),
    
    path('album/', AlbumListView.as_view(), name='store-album'),
    path('album/create', AlbumCreateView.as_view(), name='album-create'),
    path('album/<pk>/update', AlbumUpdateView.as_view(), name='album-update'),
    path('album/<pk>/delete', AlbumDeleteView.as_view(), name='album-delete'),

]
