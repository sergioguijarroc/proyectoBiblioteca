from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


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


class EditarLibro(UpdateView):
    model = Libro
    fields = ["title", "author", "rating", "sinopsis"]
    template_name = "biblioteca/editar_libro.html"
    success_url = reverse_lazy("listar_libros")  # Esto es como un redirect


"""
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
"""


class LibroDeleteView(DeleteView):
    model = Libro
    success_url = reverse_lazy("listar_libros")


class CrearLibro(View):
    def get(self, request):
        return render(
            request, template_name, {"forms": formset_factory(LibroForm, extra=3)}
        )

    def post(self, request):
        formset = formset_factory(Libro)

        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    form.save()
            return redirect(to="listar_libros")
        else:
            returnrender(request, "biblioteca/añadir_libros.html")
