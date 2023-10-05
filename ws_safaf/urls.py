from django.urls import path, include
from .views import *

# specify URL Path for rest_framework
urlpatterns = [
    path('api_empleados', EmpleadosViewSet.as_view()),
    path('api_cuentas', CuentasViewSet.as_view()),
    path('api_contactos', ContactoViewSet.as_view()),
    path('api_campus', CampusViewSet.as_view()),
    path('api_bloques', BloqueViewSet.as_view()),
    path('api_espacios_fisicos', EspacioFisicoViewSet.as_view())
]