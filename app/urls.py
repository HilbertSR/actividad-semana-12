from django.urls import path
from .views import ProyectoView

urlpatterns = [
    path("Libros/", ProyectoView.as_view(), name="Libros"),
    path("Libros/<int:pk>/", ProyectoView.as_view(), name="Libros-detalle"),
]