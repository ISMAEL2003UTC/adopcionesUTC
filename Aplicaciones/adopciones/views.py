from django.shortcuts import render,redirect

from .models import Persona, Mascota, Adopcion
from django.contrib import messages
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

def eliminarMascota(request, id_mascota):
    mascotaEliminar =Mascota.objects.get(id_mascota=id_mascota)
    mascotaEliminar.delete()
    messages.success(request,"Mascota Eliminado Exitosamente")
    return redirect('/mascota')
def nuevaMascota(request):
    return render(request,"nuevaMascota.html")


def guardarMascota(request):
    # Capturar los datos del formulario
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    especie = request.POST["especie"]
    raza = request.POST["raza"]
    edad = request.POST["edad"]
    sexo = request.POST["sexo"]
    color = request.POST["color"]
    estado = request.POST["estado"]
    foto = request.FILES.get("foto")

    Mascota.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        especie=especie,
        raza=raza,
        edad=edad,
        sexo=sexo,
        color=color,
        estado=estado,
        foto=foto
    )

    messages.success(request, "Mascota registrada exitosamente.")
    return redirect("/mascota")

def editarMascota(request,id_mascota):
    mascotaEditar=Mascota.objects.get(id_mascota=id_mascota)
    return render(request,"editarMascota.html", {'mascotaEditar':mascotaEditar})

def actualizarMascota(request, id_mascota):
    id = request.POST.get("id")
    
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        especie = request.POST["especie"]
        raza = request.POST["raza"]
        edad = request.POST["edad"]
        sexo = request.POST["sexo"]
        color = request.POST["color"]
        estado = request.POST["estado"]

        mascota = Mascota.objects.get(id_mascota=id_mascota)
        mascota.nombre = nombre
        mascota.descripcion = descripcion
        mascota.especie = especie
        mascota.raza = raza
        mascota.edad = edad
        mascota.sexo = sexo
        mascota.color = color
        mascota.estado = estado

        if request.FILES.get("foto"):
            mascota.foto = request.FILES["foto"]

        mascota.save()
        messages.success(request, "Mascota actualizada exitosamente.")
        return redirect("/mascota")

    
    
