from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Libro(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    sinopsis = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  # se crea automaticamente
    updated_at = models.DateTimeField(auto_now=True)  # se actualiza automaticamente


# Create your models here.
