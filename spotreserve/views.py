from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.template import loader0
# from django.shortcuts import render
# from django.urls import reverse

from urllib import response
from django.views import generic
from .models import Spot

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'spotreserve/index.html'
    context_object_name = 'spot_objects'

    def get_queryset(self):
        return Spot.objects.order_by('spot_identification')

def spotdetail(request, spot_identification):
    return HttpResponse(f'Here is something {spot_identification}')

    # model = Spot
    # template_name = 'spotreserve/spot.html'