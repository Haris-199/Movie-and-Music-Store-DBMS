from django.views import View
from django.template.response import TemplateResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from store.models import Franchise


# List franchises by their product_id
class FranchiseListView(ListView):
    model = Franchise
    ordering = ['product_id']
    context_object_name = 'franchises'


# Render a form for creating a new franchise
class FranchiseCreateView(CreateView):
    model = Franchise
    fields = ['product_id', 'name', 'price']
    success_url = '/franchise/'


# Display franchises by searching for their name
class FranchiseSearchListView(View):
    def get(self, request):
        franchise_name = request.GET.get('name', None)
        return TemplateResponse(request, 'store/franchise_search.html', {'franchises': Franchise.objects.filter(name=franchise_name)})


# Render a form for updating an franchise
class FranchiseUpdateView(UpdateView):
    model = Franchise
    template_name = 'store/franchise_update_form.html'
    fields = ['product_id', 'name', 'price']
    success_url = '/franchise/'


# Show delete confirmation page for franchise
class FranchiseDeleteView(DeleteView):
    model = Franchise
    success_url = '/franchise/'
