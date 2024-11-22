from django.views import View
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Artist


class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'


class ArtistSearchListView(View):
    def get(self, request):
        artist_name = request.GET.get('name', None)
        return TemplateResponse(request, 'store/artist_search.html', {'artists': Artist.objects.filter(name=artist_name)})


class ArtistCreateView(CreateView):
    model = Artist
    fields = ['name', 'genres', 'listeners']
    success_url = '/artist/'

class ArtistUpdateView(UpdateView):
    model = Artist
    template_name = 'store/artist_update_form.html'
    fields = ['name', 'genres', 'listeners']
    success_url = '/artist/'


class ArtistDeleteView(DeleteView):
    model = Artist
    success_url = '/artist/'
