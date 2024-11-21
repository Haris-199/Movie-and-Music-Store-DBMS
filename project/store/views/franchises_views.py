from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Franchise


class FranchiseListView(ListView):
    model = Franchise
    ordering = ['product_id']
    context_object_name = 'franchises'


class FranchiseCreateView(CreateView):
    model = Franchise
    fields = ['product_id', 'name', 'price']
    success_url = '/franchise/'

class FranchiseUpdateView(UpdateView):
    model = Franchise
    template_name = 'store/franchise_update_form.html'
    fields = ['product_id', 'name', 'price']
    success_url = '/franchise/'


class FranchiseDeleteView(DeleteView):
    model = Franchise
    success_url = '/franchise/'
