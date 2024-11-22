from django.views import View
from django.template.response import TemplateResponse
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


class MovieSearchListView(View):
    def get(self, request):
        movie_name = request.GET.get('name', None)
        return TemplateResponse(request, 'store/movie_search.html', {'movies': Movie.objects.filter(name=movie_name)})


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'store/movie_update_form.html'
    fields = ['product_id', 'name', 'genre', 'director', 'actors', 'price', 'franchise']
    success_url = '/movie/'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = '/movie/'
