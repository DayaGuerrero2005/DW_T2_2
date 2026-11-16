from django.http import JsonResponse
from django.conf import settings

def panel_alertas(request):
    if not getattr(settings, 'ENABLE_NOTIFICATIONS', False):
        return JsonResponse({'error': 'Módulo de notificaciones deshabilitado en la variante activa.'}, status=403)
    return JsonResponse({
        'alertas_activas': [
            {'codigo': 'ALR-01', 'mensaje': 'Paciente en Nivel II requiere reevaluación en 15 min', 'prioridad': 'Alta'},
            {'codigo': 'ALR-02', 'mensaje': 'Stock de insumos de triaje al 82% en bodega central', 'prioridad': 'Media'},
        ]
    })
