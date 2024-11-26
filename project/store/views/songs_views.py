from django.views import View
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Song


# List songs by their product_id
class SongListView(ListView):
    model = Song
    ordering = ['product_id']
    context_object_name = 'songs'


# Display songs by searching for their name
class SongSearchListView(View):
    def get(self, request):
        song_name = request.GET.get('name', None)
        return TemplateResponse(request, 'store/song_search.html', {'songs': Song.objects.filter(name=song_name)})


# Render a form for creating a new song
class SongCreateView(CreateView):
    model = Song
    fields = ['product_id', 'name', 'artist', 'genre', 'album', 'price']
    success_url = '/song/'


# Render a form for updating an song
class SongUpdateView(UpdateView):
    model = Song
    template_name = 'store/song_update_form.html'
    fields = ['product_id', 'name', 'artist', 'genre', 'album', 'price']
    success_url = '/song/'


# Show delete confirmation page for song
class SongDeleteView(DeleteView):
    model = Song
    success_url = '/song/'
