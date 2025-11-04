from django.shortcuts import render, redirect
from django.contrib import messages

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

def crear_adopciones(request):
    mascotas = Mascota.objects.all()
    personas = Persona.objects.all()
    return render(request,'adopciones/createAdopciones.html',{'mascotas':mascotas,'personas':personas})

"""def guardar_adopciones(request):
    personas_id = request.POST.get('personas')
    mascotas_id = request.POST.get('mascotas')
    fecha_adopcion = request.POST.get('fecha_adopcion')
    observaciones = request.POST.get('observaciones')
    

    persona = Persona.objects.get(id_persona=personas_id)
    mascota = Mascota.objects.get(id=mascotas_id)
    adopcion = Adopcion.objects.create(
        id_persona=persona,
        id_mascota=mascota,
        fecha_adopcion=fecha_adopcion,
        observaciones=observaciones
    )
    

    messages.success(request, 'Adopción creada correctamente')
    return redirect('/listar-adopciones')
"""
def guardar_adopciones(request):
    personas_id = request.POST.get('personas')
    mascotas_id = request.POST.get('mascotas')
    fecha_adopcion = request.POST.get('fecha_adopcion')
    observaciones = request.POST.get('observaciones')

    persona = Persona.objects.get(id_persona=personas_id)
    mascota = Mascota.objects.get(id=mascotas_id)

    #  Verificar si la persona ya adoptó esa mascota
    if Adopcion.objects.filter(id_persona=persona, id_mascota=mascota).exists():
        messages.error(request, 'Esta persona ya adoptó esta mascota.')
        return redirect('/crear-adopciones')

    # Verificar si la mascota ya fue adoptada por alguien más
    if Adopcion.objects.filter(id_mascota=mascota).exists():
        messages.error(request, 'Esta mascota ya fue adoptada por otra persona.')
        return redirect('/crear-adopciones')

    #  Crear la adopción
    adopcion = Adopcion.objects.create(
        id_persona=persona,
        id_mascota=mascota,
        fecha_adopcion=fecha_adopcion,
        observaciones=observaciones
    )

    # Cambiar estado de la mascota
    mascota.estado = 'Adoptada'
    mascota.save()

    messages.success(request, 'Adopción registrada correctamente.')
    return redirect('/listar-adopciones')

def eliminar_adopciones(request,id):
    adopcion = Adopcion.objects.get(id=id)
    nombre = adopcion.id_mascota.nombre
    adopcion.delete()
    messages.success(request, f'Adopcion de mascota  {nombre} eliminado correctamente')
    return redirect('/listar-adopciones')
