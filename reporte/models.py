from django.db import models

# Create your models here.

class Ordenes(models.Model):
    # Define los campos de tu tabla aquí
    canal = models.CharField(max_length=4000)
    numero_orden = models.CharField(primary_key=True, max_length=4000)

    class Meta:
        # Especifica el nombre de la tabla en la base de datos
        db_table = 'oc_ordenes_cons'

    def __str__(self):
        # Representación de cadena del objeto
        return self.numero_orden
