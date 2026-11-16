from django.apps import AppConfig

class MedicalCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.medical_core'
    label = 'medical_core'
    verbose_name = 'Núcleo de Registro de Atenciones y Triaje Clínico'
