from django.shortcuts import render
from django.conf import settings

def dashboard_atenciones(request):
    """
    Vista principal del núcleo clínico. Evalúa dinámicamente las banderas
    ENABLE_REPORTS, ENABLE_NOTIFICATIONS y ENABLE_ADVANCED_SEARCH definidas
    en settings.py / config_product.py.
    """
    atenciones = [
        {
            'ficha': 'ATN-2026-0891',
            'paciente': 'Sgto. Carlos Mendoza V.',
            'area': 'Emergencias / Trauma',
            'triaje': 'Nivel II (Urgencia)',
            'profesional': 'TEM. Dayanara Guerrero',
            'estado': 'Estabilizado',
        },
        {
            'ficha': 'ATN-2026-0892',
            'paciente': 'Cbos. Andrea Villacís R.',
            'area': 'Consulta General',
            'triaje': 'Nivel IV (Estándar)',
            'profesional': 'TEM. Eduardo Quinteros',
            'estado': 'Alta Médica',
        },
        {
            'ficha': 'ATN-2026-0893',
            'paciente': 'Tnte. Roberto Salazar P.',
            'area': 'Cardiología / Control',
            'triaje': 'Nivel III (Observación)',
            'profesional': 'Dra. Gleyder Lescano',
            'estado': 'En Evaluación',
        },
        {
            'ficha': 'ATN-2026-0894',
            'paciente': 'Subt. Sofía Zambrano L.',
            'area': 'Salud Ocupacional',
            'triaje': 'Nivel V (No Urgente)',
            'profesional': 'Dr. Kevin Barboza',
            'estado': 'Completado',
        },
    ]

    q = request.GET.get('q', '').strip()
    if q and getattr(settings, 'ENABLE_ADVANCED_SEARCH', False):
        atenciones = [
            a for a in atenciones
            if q.lower() in a['paciente'].lower() or q.lower() in a['ficha'].lower()
        ]

    context = {
        'variant_code': getattr(settings, 'VARIANT_CODE', 'PRODUCT_B'),
        'variant_name': getattr(settings, 'VARIANT_NAME', 'Variante A'),
        'enable_reports': settings.ENABLE_REPORTS,
        'enable_notifications': getattr(settings, 'ENABLE_NOTIFICATIONS', False),
        'enable_advanced_search': getattr(settings, 'ENABLE_ADVANCED_SEARCH', False),
        'optional_apps_count': len(getattr(settings, 'OPTIONAL_APPS', [])),
        'atenciones': atenciones,
        'q': q,
    }
    if settings.ENABLE_REPORTS:
        context['formatos_exportacion'] = ['PDF Institucional', 'CSV Estadístico', 'Ficha HL7/JSON']
    return render(request, 'medical_core/dashboard.html', context)
