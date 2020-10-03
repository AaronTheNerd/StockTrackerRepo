from django.shortcuts import render

# Create your views here.
from home.models import Stock

def index(request):
    """View function for search page of site."""
    return render(request, 'index.html')

from django.views import generic

class SearchView(generic.ListView):
    model = Stock
    template_name = "search_view.html"