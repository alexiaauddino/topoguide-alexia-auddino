from django.urls import path

from . import views

urlpatterns = [
    path('itineraires/', views.itineraires, name='itineraires'),
    #path('<int:itineraire_id>/', views.sorties, name='sorties'),
]