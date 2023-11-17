from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from biblioteca.forms import FormularioLibros

# from .forms import FormularioLibro
from .models import Libro

# Create your views here.

"""
class Listar_libros(View):
    def get(self, request):
        libros = Libro.objects.all()
        return render(request, "biblioteca/listar_libros.html", {"libros": libros})
"""


class Listar_libros(ListView):
    model = Libro


class Añadir_libros(View):
    template_name = "biblioteca/añadir_libros.html"
    form = FormularioLibros()

    def get(self, request):
        form = self.form
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = FormularioLibros(request.POST)
        if form.is_valid():
            form.save()
            return redirect("añadir_libros")
        return render(request, self.template_name, {"form": form})


"""
class DetalleLibro(View):
    def get(self, request, pk):
        libro = Libro.objects.get(pk=pk)
        return render(request, "biblioteca/detalle_libro.html", {"libro": libro})
"""


class DetalleLibro(DetailView):
    model = Libro


class EditarLibro(View):
    template_name = "biblioteca/editar_libro.html"

    def get(self, request, pk):
        libro_editar = get_object_or_404(Libro, pk=pk)
        form = FormularioLibros(instance=libro_editar)
        return render(
            request, self.template_name, {"form": form, "libro": libro_editar}
        )

    def post(self, request, pk):
        libro_editar = get_object_or_404(Libro, pk=pk)
        form = FormularioLibros(request.POST, instance=libro_editar)
        if form.is_valid:
            form.save()
            return redirect("detalle_libro", pk=libro_editar.pk)
