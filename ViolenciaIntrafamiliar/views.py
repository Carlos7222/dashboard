from django.shortcuts import render,redirect
from .models import ViolenciaIntrafamiliar

# Create your views here.
def home(request):
    Intrafamiliar=ViolenciaIntrafamiliar.objects.all()
    return render(request,"violenciaHome.html", {"muertes":Intrafamiliar})

def registraViolencia(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    AdultoMayor=request.POST['AdultoMayor']
    NiñoAdolecente=request.POST['NiñoAdolecente']
    OtrosFamiliares=request.POST['OtrosFamiliares']
    Pareja=request.POST['Pareja']
    Intrafamiliar=ViolenciaIntrafamiliar.objects.create(ano=ano,Ncasos=Ncasos,AdultoMayor=AdultoMayor,NiñoAdolecente=NiñoAdolecente,OtrosFamiliares=OtrosFamiliares,Pareja=Pareja)
    return redirect(home)

def eliminarViolencia(request,ano):
    MuertedDelete=ViolenciaIntrafamiliar.objects.get(ano=ano)
    MuertedDelete.delete()
    return redirect(home)

def editarViolencia(request,ano):
    muerteEdit=ViolenciaIntrafamiliar.objects.get(ano=ano)
    return render(request,"violenciaEdicion.html", {"violencia":muerteEdit})


def editarCompleto(request):
    ano=request.POST['ano']
    Ncasos=request.POST['Ncasos']
    AdultoMayor=request.POST['AdultoMayor']
    NiñoAdolecente=request.POST['NiñoAdolecente']
    OtrosFamiliares=request.POST['OtrosFamiliares']
    Pareja=request.POST['Pareja']
    
    actualizarobjeto=ViolenciaIntrafamiliar.objects.get(ano=ano)
    actualizarobjeto.Ncasos=Ncasos
    actualizarobjeto.AdultoMayor=AdultoMayor
    actualizarobjeto.NiñoAdolecente=NiñoAdolecente
    actualizarobjeto.OtrosFamiliares=OtrosFamiliares
    actualizarobjeto.Pareja=Pareja
    actualizarobjeto.save()
    
    return redirect(home)