from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Itineraire

# Create your views here.

def itineraires(request):
    template = loader.get_template('itineraires/itineraires.html')
    if request.method == 'GET': # If the form is submitted
        search = request.GET.get('search', None)
        itineraire_list = Itineraire.objects.order_by('titre')[:]
        context = {
            'itineraire_list': itineraire_list,
            'search' : search,
        }
    else:
        itineraire_list = Itineraire.objects.order_by('titre')[:]
        context = {
            'itineraire_list': itineraire_list,
        }
    return HttpResponse(template.render(context, request))