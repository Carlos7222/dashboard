from django.shortcuts import render,redirect
from .models import MuertesViolentas
# Create your views here.
def home(request):
    Muerteviolentas=MuertesViolentas.objects.all()
    return render(request,"muerteshome.html", {"muertes":Muerteviolentas})

def registrarMuerte(request):
    ano=request.POST['ano']
    personas=request.POST['personas']
    suicidios=request.POST['suicidios']
    muertesAccidentes=request.POST['muertesAccidentes']
    muerteTransporte=request.POST['muerteTransporte']
    homicidio=request.POST['homicidio']
    MuerteViolentaRegistro=MuertesViolentas.objects.create(ano=ano,personas=personas,suicidios=suicidios,muertesAccidentes=muertesAccidentes,muerteTransporte=muerteTransporte,homicidio=homicidio)
    return redirect(home)

def eliminarMuerte(request,ano):
    MuertedDelete=MuertesViolentas.objects.get(ano=ano)
    MuertedDelete.delete()
    return redirect(home)

def editarMuertes(request,ano):
    muerteEdit=MuertesViolentas.objects.get(ano=ano)
    return render(request,"edicionMuerte.html", {"muertes":muerteEdit})


def editarCompleto(request):
    ano=request.POST['ano']
    personas=request.POST['personas']
    suicidios=request.POST['suicidios']
    muertesAccidentes=request.POST['muertesAccidentes']
    muerteTransporte=request.POST['muerteTransporte']
    homicidio=request.POST['homicidio']
    
    actualizarobjeto=MuertesViolentas.objects.get(ano=ano)
    actualizarobjeto.personas=personas
    actualizarobjeto.suicidios=suicidios
    actualizarobjeto.muertesAccidentes=muertesAccidentes
    actualizarobjeto.muerteTransporte=muerteTransporte
    actualizarobjeto.homicidio=homicidio
    actualizarobjeto.save()
    
    return redirect(home)