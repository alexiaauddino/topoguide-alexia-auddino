from django.urls import path

from . import views

urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    path('sorties/<int:itineraire_id>/sortie/<int:sortie_id>/', views.details, name='details'),
    path('sorties/<int:itineraire_id>/nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie'),
]