from django.urls import path, include
from .views import *

# specify URL Path for rest_framework
urlpatterns = [
    path('api_empleados', EmpleadosViewSet.as_view()),
    path('api_cuentas', CuentasViewSet.as_view())
]