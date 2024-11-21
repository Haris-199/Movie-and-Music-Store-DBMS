from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Song


class SongListView(ListView):
    model = Song
    ordering = ['product_id']
    context_object_name = 'songs'


class SongCreateView(CreateView):
    model = Song
    fields = ['product_id', 'name', 'artist', 'genre', 'album', 'price']
    success_url = '/song/'

class SongUpdateView(UpdateView):
    model = Song
    template_name = 'store/song_update_form.html'
    fields = ['product_id', 'name', 'artist', 'genre', 'album', 'price']
    success_url = '/song/'


class SongDeleteView(DeleteView):
    model = Song
    success_url = '/song/'
