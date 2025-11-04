
from django.urls import path
from .import views

urlpatterns = [
    path('persona/', views.persona, name='persona'),
    path('mascota/', views.mascota, name='mascota'),
    
    #adopciones
   
    path('listar-adopciones',views.listar_adopciones),
    path('crear-adopciones',views.crear_adopciones),
    path('guardar-adopciones',views.guardar_adopciones),
    path('eliminar-adopciones/<id>',views.eliminar_adopciones),
    #path('editar-adopciones/<id>',views.editar_adopciones),
    #path('procesar-info-adopciones',views.procesar_info_adopciones),

    
]
