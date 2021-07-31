from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombreEmpresa = models.CharField("Nombre de la empresa", max_length=255)
    direccion =  models.CharField("Direccion de la empresa", max_length=255)
    nit =  models.CharField("Nit de la empresa", max_length=255)
    telefono =  models.CharField("Telefono de la empresa", max_length=255)
      

    def __str__(self):
        return self.nombreEmpresa

