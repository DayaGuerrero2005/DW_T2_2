from django.db import models

class AtencionMedica(models.Model):
    codigo_ficha = models.CharField(max_length=20, unique=True)
    paciente = models.CharField(max_length=120)
    unidad_policial = models.CharField(max_length=80)
    nivel_triaje = models.CharField(max_length=25)
    diagnostico = models.CharField(max_length=200)
    profesional = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo_ficha} - {self.paciente}"
