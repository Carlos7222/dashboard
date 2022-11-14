from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarDelitoSexuales/',views.registrarDelitoSexuales),
        path('eliminarDelitoSexuales/<ano>',views.eliminarDelitoSexuales),
         path('editarDelitoSexuales/<ano>',views.editarDelitoSexuales),
        path('editarDelitoSexuales/',views.editarCompleto)
             ]