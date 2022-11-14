from django.shortcuts import render,redirect
from .models import Hurtos
# Create your views here.
def home(request):
    Intrafamiliar=Hurtos.objects.all()
    return render(request,"hurtosHome.html", {"muertes":Intrafamiliar})

def homeprincipal(request):
    return render(request,"home.html")

def registrarHurtos(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    residencia=request.POST['residencia']
    personas=request.POST['personas']
    comercio=request.POST['comercio']
    automotores=request.POST['automotores']
    Intrafamiliar=Hurtos.objects.create(ano=ano,Ncasos=Ncasos,residencia=residencia,personas=personas,comercio=comercio,automotores=automotores)
    return redirect(home)

def eliminarHurtos(request,ano):
    MuertedDelete=Hurtos.objects.get(ano=ano)
    MuertedDelete.delete()
    return redirect(home)

def editarHurtos(request,ano):
    muerteEdit=Hurtos.objects.get(ano=ano)
    return render(request,"hurtosEdicion.html", {"violencia":muerteEdit})


def editarCompleto(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    residencia=request.POST['residencia']
    personas=request.POST['personas']
    comercio=request.POST['comercio']
    automotores=request.POST['automotores']
    
    actualizarobjeto=Hurtos.objects.get(ano=ano)
    actualizarobjeto.Ncasos=Ncasos
    actualizarobjeto.residencia=residencia
    actualizarobjeto.personas=personas
    actualizarobjeto.comercio=comercio
    actualizarobjeto.automotores=automotores
    actualizarobjeto.save()
    
    return redirect(home)