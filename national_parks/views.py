from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
import json


from .models import Park

# Create your views here.

def home_page(request):
    return render(request, 'search/search_page.html')


# Used to turn a park into JSON
class ParkJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Park):
            return obj.__dict__


def search_park(request):

    park = request.GET.get('query')   # This is sent with the AJAX query.

    if park:
        # DB query
        parks = Park.objects.filter(name__icontains=park)
    else:
        # No search query, return everything. Adapt to suit the behavior of your app.
        # Everything could be a lot! You would probably want to limit to (e.g.) the first 30 results
        parks = Park.objects.all()

    # Sort by name and convert to a list
    parks = list(parks.order_by('name'))

    # Use parkJSONEncoder to convert list of parks to JSON. Return JSON object.
    return JsonResponse(parks, encoder=ParkJSONEncoder, safe=False)
