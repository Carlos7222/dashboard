from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarMuertes/',views.registrarMuerte),
        path('eliminarMuertes/<ano>',views.eliminarMuerte),
         path('editarMuertes/<ano>',views.editarMuertes),
        path('editarComplete/',views.editarCompleto)
            
             ]