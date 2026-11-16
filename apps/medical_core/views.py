from django.shortcuts import render
from django.conf import settings

def dashboard_atenciones(request):
    """
    Vista principal del núcleo clínico. Evalúa dinámicamente las banderas
    ENABLE_REPORTS y ENABLE_NOTIFICATIONS definidas en settings.py / config_product.py.
    """
    context = {
        'variant_name': getattr(settings, 'VARIANT_NAME', 'Variante A'),
        'enable_reports': settings.ENABLE_REPORTS,
        'enable_notifications': getattr(settings, 'ENABLE_NOTIFICATIONS', False),
        'atenciones': [
            {'ficha': 'ATN-2026-0891', 'paciente': 'Sgto. Carlos Mendoza V.', 'area': 'Emergencias / Trauma', 'triaje': 'Nivel II - Naranja', 'profesional': 'TEM. Dayanara Guerrero', 'estado': 'Estabilizado'},
            {'ficha': 'ATN-2026-0892', 'paciente': 'Cbos. Andrea Villacís R.', 'area': 'Consulta General', 'triaje': 'Nivel IV - Verde', 'profesional': 'TEM. Dayanara Guerrero', 'estado': 'Alta Médica'},
            {'ficha': 'ATN-2026-0893', 'paciente': 'Tnte. Roberto Salazar P.', 'area': 'Cardiología / Control', 'triaje': 'Nivel III - Amarillo', 'profesional': 'Dr. Marcos Cevallos', 'estado': 'En Observación'},
            {'ficha': 'ATN-2026-0894', 'paciente': 'Subt. Sofía Zambrano L.', 'area': 'Salud Ocupacional', 'triaje': 'Nivel V - Azul', 'profesional': 'TEM. Dayanara Guerrero', 'estado': 'Completado'},
        ]
    }
    if settings.ENABLE_REPORTS:
        context['formatos_exportacion'] = ['PDF Institucional', 'CSV Estadístico', 'Ficha HL7/JSON']
    return render(request, 'medical_core/dashboard.html', context)
