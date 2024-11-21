from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Album


class AlbumListView(ListView):
    model = Album
    ordering = ['product_id']
    context_object_name = 'albums'


class AlbumCreateView(CreateView):
    model = Album
    fields = ['product_id', 'name', 'artist', 'price']
    success_url = '/album/'

class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['product_id', 'name', 'artist', 'price']
    success_url = '/album/'


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/album/'
