from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('registrarViolencia/',views.registrarMatriculaEscolar),
        path('eliminarViolencia/<ano>',views.eliminarMatriculaEscolar),
         path('editarViolencia/<ano>',views.editarMatriculaEscolar),
        path('editarViolencia/',views.editarCompleto)
             ]