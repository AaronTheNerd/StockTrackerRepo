from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from home.models import Stock

def index(request):
    """View function for search page of site."""
    return render(request, 'index.html')

FILTERS = (('symbol', 'Symbol: A-Z'),
          ('-symbol', 'Symbol: Z-A'),
          ('-current_price', 'Price: High to Low'),
          ('current_price', 'Price: Low to High'))

def search(request):
    context = {'stocks':Stock.objects.all().order_by('symbol'), 'filters':FILTERS}
    if request.method == 'GET':
        context['query'] = request.GET.get('q')
        context['curr_filter'] = request.GET.get('filter')
        context['submitbutton'] = request.GET.get('submit')
        if context['query'] is not None:
            results = Stock.objects.filter(Q(symbol__icontains=context['query'])).distinct()
            if context['curr_filter']:
                context['results'] = results.order_by(context['curr_filter'])
            else:
                context['results'] = results.order_by(FILTERS[0][0])
            return render(request, 'search_view.html', context)    
    return render(request, 'search_view.html', context)
