from django.views import View
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Album


# List albums by their product_id
class AlbumListView(ListView):
    model = Album
    ordering = ['product_id']
    context_object_name = 'albums'


# Display albums by searching for their name
class AlbumSearchListView(View):
    def get(self, request):
        album_name = request.GET.get('name', None)
        return TemplateResponse(request, 'store/album_search.html', {'albums': Album.objects.filter(name=album_name)})


# Render a form for creating a new album
class AlbumCreateView(CreateView):
    model = Album
    fields = ['product_id', 'name', 'artist', 'price']
    success_url = '/album/'


# Render a form for updating an album
class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'store/album_update_form.html'
    fields = ['product_id', 'name', 'artist', 'price']
    success_url = '/album/'


# Show delete confirmation page for album
class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/album/'
