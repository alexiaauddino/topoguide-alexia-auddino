from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import SortieForm
from .models import Itineraire, Sortie

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


def sorties(request, itineraire_id):
    try:
        itineraire= Itineraire.objects.get(pk=itineraire_id)
        sorties_list = Sortie.objects.filter(itineraire=itineraire).all()
    except Itineraire.DoesNotExist:
        raise Http404("L'itinéraire n'existe pas")
    return render(request, 'itineraires/sorties.html', {'itineraire': itineraire, 'sorties_list': sorties_list})


def details(request, sortie_id, itineraire_id):
    try:
        sortie_detail = Sortie.objects.get(pk=sortie_id)
    except Sortie.DoesNotExist:
        raise Http404("La sortie n'existe pas")
    return render(request, 'itineraires/details.html', {'sortie_detail' : sortie_detail, 'itineraire_id' : itineraire_id})

@login_required
def nouvelle_sortie(request, itineraire_id):
    submitted = False
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid :
            form = form.save(commit=False)
            form.utilisateur = request.user
            form.itineraire = Itineraire.objects.get(pk=itineraire_id)
            form.save()
            submitted = True
    else : 
        form = SortieForm
        if submitted in request.GET:
            submitted = True
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form, 'itineraire_id' : itineraire_id, 'submitted' : submitted})

@login_required
def modif_sortie(request, itineraire_id, sortie_id):
    submitted = False
    sortie = get_object_or_404(Sortie, id=sortie_id)
    if request.method == 'POST':
        form = SortieForm(request.POST or None, instance=sortie)
        if form.is_valid :
            form = form.save(commit=False)
            form.utilisateur = request.user
            form.itineraire = Itineraire.objects.get(pk=itineraire_id)
            form.save()
            submitted=True
    else : 
        form = SortieForm(request.POST or None, instance=sortie)
    return render(request, 'itineraires/nouvelle_sortie.html', {'form' : form, 'itineraire_id' : itineraire_id, 'sortie_id' : sortie_id, 'submitted' : submitted})