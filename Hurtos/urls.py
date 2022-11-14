from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarHurtos/',views.registrarHurtos),
        path('eliminarHurtos/<ano>',views.eliminarHurtos),
         path('editarHurtos/<ano>',views.editarHurtos),
        path('editarHurtos/',views.editarCompleto)
             ]