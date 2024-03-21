from django.db import models

# Create your models here.

class Ordenes(models.Model):
    # Define los campos de tu tabla aquí
    CANAL = models.CharField(max_length=4000)
    NUMERO_ORDEN = models.CharField(primary_key=True, max_length=4000)

    class Meta:
        # Especifica el nombre de la tabla en la base de datos
        db_table = 'OC_ORDENES_CONS'

    def __str__(self):
        # Representación de cadena del objeto
        return self.NUMERO_ORDEN
