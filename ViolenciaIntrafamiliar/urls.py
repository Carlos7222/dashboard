from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarViolencia/',views.registraViolencia),
        path('eliminarViolencia/<ano>',views.eliminarViolencia),
         path('editarViolencia/<ano>',views.editarViolencia),
        path('editarViolencia/',views.editarCompleto)
             ]