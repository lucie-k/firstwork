from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('liste/',views.listeEtudiants,name="liste"),
    path('loyer/',views.loyer,name='loyer'),
    path('predire/',views.predire,name='predire')
]