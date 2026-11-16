from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings

def exportar_reporte_pdf(request):
    if not getattr(settings, 'ENABLE_REPORTS', False):
        return HttpResponseForbidden('La característica ENABLE_REPORTS está desactivada en esta variante.')
    return HttpResponse('Reporte PDF generado exitosamente por apps.reports.', content_type='application/pdf')

def exportar_reporte_csv(request):
    if not getattr(settings, 'ENABLE_REPORTS', False):
        return HttpResponseForbidden('La característica ENABLE_REPORTS está desactivada en esta variante.')
    return HttpResponse('ficha,paciente,triaje,estado\nATN-2026-0891,Carlos Mendoza,Nivel II,Estabilizado', content_type='text/csv')
