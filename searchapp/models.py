# Import necessary modules
from django.db import models
from django.urls import  reverse

# Create model gor newtype
class Booktype(models.Model):
    btype = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering=('btype',)

# Create model gor new
class New(models.Model):
    palabra = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)
    url = models.TextField()
    # type = models.ForeignKey(Booktype, on_delete=models.CASCADE)
    fecha = models.DateField()

    class Meta:
        ordering=('fecha',)

    def __str__(self):
        return self.titulo

    def get_url(self):
       return reverse('new_detail', args=[self.id])