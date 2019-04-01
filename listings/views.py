from django.shortcuts import render
from .models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.all()

    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    context = {
        'listing' : listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    context = {
        'state_choices': state_choices,
        'bedroom-choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)