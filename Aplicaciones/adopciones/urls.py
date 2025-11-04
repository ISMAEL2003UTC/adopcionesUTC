
from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('persona/', views.persona, name='persona'),
    path('mascota/', views.mascota, name='mascota'),
    path('adopcion/', views.adopcion, name='adopcion'),
    path('nuevaAdopcion/', views.nuevaAdopcion, name='nuevaAdopcion'),
    path('eliminarMascota/<id_mascota>', views.eliminarMascota),
    path('nuevaMascota/', views.nuevaMascota, name='nuevaMascota'),
    path('guardarMascota/', views.guardarMascota, name='guardarMascota'),
    path('editarMascota/<id_mascota>', views.editarMascota, name='editarMascota'),
    path('actualizarMascota/<id_mascota>/', views.actualizarMascota, name='actualizarMascota'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)