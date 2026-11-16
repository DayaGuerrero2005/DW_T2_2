from django.apps import AppConfig

class FileManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.file_manager'
    label = 'file_manager'
    verbose_name = 'Carga y Validación de Archivos Adjuntos (Reutilizable)'
