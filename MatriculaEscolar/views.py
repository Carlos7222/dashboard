from django.shortcuts import render,redirect
from .models import MatriculaEscolares
# Create your views here.
def home(request):
    Muerteviolentas=MatriculaEscolares.objects.all()
    return render(request,"MatriculasHome.html", {"muertes":Muerteviolentas})

def registrarMatriculaEscolar(request):
    ano=request.POST['ano']
    Nmatriculados=request.POST['Nmatriculados']
    preescolar=request.POST['preescolar']
    primaria=request.POST['primaria']
    basicaSecundarioa=request.POST['basicaSecundarioa']
    media=request.POST['media']
    MuerteViolentaRegistro=MatriculaEscolares.objects.create(ano=ano,Nmatriculados=Nmatriculados,preescolar=preescolar,primaria=primaria,basicaSecundarioa=basicaSecundarioa,media=media)
    return redirect(home)

def eliminarMatriculaEscolar(request,ano):
    MuertedDelete=MatriculaEscolares.objects.get(ano=ano)
    MuertedDelete.delete()
    return redirect(home)

def editarMatriculaEscolar(request,ano):
    muerteEdit=MatriculaEscolares.objects.get(ano=ano)
    return render(request,"MatriculasEdicion.html", {"muertes":muerteEdit})


def editarCompleto(request): 
    ano=request.POST['ano']
    Nmatriculados=request.POST['Nmatriculados']
    preescolar=request.POST['preescolar']
    primaria=request.POST['primaria']
    basicaSecundarioa=request.POST['basicaSecundarioa']
    media=request.POST['media']
    
    actualizarobjeto=MatriculaEscolares.objects.get(ano=ano)
    actualizarobjeto.Nmatriculados=Nmatriculados
    actualizarobjeto.preescolar=preescolar
    actualizarobjeto.primaria=primaria
    actualizarobjeto.basicaSecundarioa=basicaSecundarioa
    actualizarobjeto.media=media
    actualizarobjeto.save()
    
    return redirect(home)