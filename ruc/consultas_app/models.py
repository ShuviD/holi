from django.db import models

class rucs(models.Model):
    ruc = models.DecimalField(primary_key=True, max_digits=11, decimal_places=0)
    razon_social = models.CharField(max_length=255)
    estado_del_contribuyente = models.CharField(max_length=255)
    condicion_de_domicilio = models.CharField(max_length=255)
    ubigeo = models.CharField(max_length=6)
    tipo_via = models.CharField(max_length=255)
    nombre_via = models.CharField(max_length=255)
    codigo_zona = models.CharField(max_length=255)
    tipo_zona = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    interior = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    manzana = models.CharField(max_length=255)
    kilometro = models.CharField(max_length=255)