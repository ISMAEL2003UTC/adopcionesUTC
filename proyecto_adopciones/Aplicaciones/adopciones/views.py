from django.shortcuts import render

from .models import Persona, Mascota, Adopcion

# Create your views here.
# renderizando el listado de adopciones
def persona(request):
    listadoPersona = Persona.objects.all()
    return render(request, 'persona.html', {'personas': listadoPersona})
def mascota(request):
    listadoMascota = Mascota.objects.all()
    return render(request, 'mascota.html', {'mascotas': listadoMascota})
def adopcion(request):
    listadoAdopcion = Adopcion.objects.all()
    return render(request, 'adopcion.html', {'adopciones': listadoAdopcion})


def nuevaAdopcion(request):
    return render(request, 'nuevaAdopcion.html')

def listar_adopciones(request):
    adopciones = Adopcion.objects.all()
    return render(request,'adopciones/indexAdopciones.html',{'adopciones':adopciones})