"""from django.urls import path
from .views import mostrar_ruc

urlpatterns = [
    # Otras rutas de tu aplicación
    path('ruc/<ruc>/', mostrar_ruc, name='detalle_ruc'),
]
"""

from django.urls import path
from .views import mostrar_ruc

urlpatterns = [
    path('ruc/<str:ruc>/', mostrar_ruc, name='mostrar_ruc'),
]
