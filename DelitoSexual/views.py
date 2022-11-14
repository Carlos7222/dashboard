from django.shortcuts import render,redirect
from .models import DelitoSexuales
# Create your views here.
def home(request):
    Intrafamiliar=DelitoSexuales.objects.all()
    return render(request,"DelitoSexualHome.html", {"muertes":Intrafamiliar})

def registrarDelitoSexuales(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    hombres=request.POST['hombres']
    mujeres=request.POST['mujeres']
    Intrafamiliar=DelitoSexuales.objects.create(ano=ano,Ncasos=Ncasos,hombres=hombres,mujeres=mujeres)
    return redirect(home)

def eliminarDelitoSexuales(request,ano):
    MuertedDelete=DelitoSexuales.objects.get(ano=ano)
    MuertedDelete.delete()
    return redirect(home)

def editarDelitoSexuales(request,ano):
    muerteEdit=DelitoSexuales.objects.get(ano=ano)
    return render(request,"DelitoSexualEdicion.html", {"violencia":muerteEdit})


def editarCompleto(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    hombres=request.POST['hombres']
    mujeres=request.POST['mujeres']
    
    
    actualizarobjeto=DelitoSexuales.objects.get(ano=ano)
    actualizarobjeto.Ncasos=Ncasos
    actualizarobjeto.hombres=hombres
    actualizarobjeto.mujeres=mujeres
    actualizarobjeto.save()
    
    return redirect(home)