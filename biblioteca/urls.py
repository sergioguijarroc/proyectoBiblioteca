from django.urls import path
from .views import Listar_libros, Añadir_libros, DetalleLibro, EditarLibro

urlpatterns = [
    path("", Listar_libros.as_view(), name="listar_libros"),
    path("añadir/", Añadir_libros.as_view(), name="añadir_libros"),
    path("detalle/<int:pk>", DetalleLibro.as_view(), name="detalle_libro"),
    path("editar/<int:pk>", EditarLibro.as_view(), name="editar_libro"),
]
