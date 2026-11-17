from django.conf import settings

def spl_feature_flags(request):
    """Inyecta las banderas de variabilidad SPL en todas las plantillas Django."""
    return {
        'VARIANT_CODE': getattr(settings, 'VARIANT_CODE', 'PRODUCT_B'),
        'VARIANT_NAME': getattr(settings, 'VARIANT_NAME', 'Variante Estándar'),
        'ENABLE_REPORTS': getattr(settings, 'ENABLE_REPORTS', False),
        'ENABLE_NOTIFICATIONS': getattr(settings, 'ENABLE_NOTIFICATIONS', False),
        'ENABLE_ADVANCED_SEARCH': getattr(settings, 'ENABLE_ADVANCED_SEARCH', False),
        'OPTIONAL_APPS_COUNT': len(getattr(settings, 'OPTIONAL_APPS', [])),
    }
