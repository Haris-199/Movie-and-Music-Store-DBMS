from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Movie


class MovieListView(ListView):
    model = Movie
    ordering = ['product_id']
    context_object_name = 'movies'


class MovieCreateView(CreateView):
    model = Movie
    fields = ['product_id', 'name', 'genre', 'director', 'actors', 'price', 'franchise']
    success_url = '/movie/'

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'store/movie_update_form.html'
    fields = ['product_id', 'name', 'genre', 'director', 'actors', 'price', 'franchise']
    success_url = '/movie/'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/movie/'
