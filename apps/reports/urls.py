from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('exportar/pdf/', views.exportar_reporte_pdf, name='export_pdf'),
    path('exportar/csv/', views.exportar_reporte_csv, name='export_csv'),
]
