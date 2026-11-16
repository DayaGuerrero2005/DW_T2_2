# medispl_unemi/config_product.py
"""
Definición centralizada de variantes para la Línea de Productos de Software (SPL).
Práctica 4 - Gestión de la Configuración de Software (UNEMI).
"""

PRODUCT_A = {
    'VARIANT_CODE': 'PRODUCT_A',
    'VARIANT_NAME': 'Variante A — Sistema Básico (Core Clínico)',
    'ENABLE_REPORTS': False,
    'ENABLE_NOTIFICATIONS': False,
    'ENABLE_ADVANCED_SEARCH': False,
}

PRODUCT_B = {
    'VARIANT_CODE': 'PRODUCT_B',
    'VARIANT_NAME': 'Variante B — Sistema Completo (Edición Extendida)',
    'ENABLE_REPORTS': True,
    'ENABLE_NOTIFICATIONS': True,
    'ENABLE_ADVANCED_SEARCH': True,
}

AVAILABLE_VARIANTS = {
    'PRODUCT_A': PRODUCT_A,
    'PRODUCT_B': PRODUCT_B,
}

def get_product_config(variant_key: str = 'PRODUCT_B') -> dict:
    """Retorna el diccionario de características de la variante seleccionada."""
    return AVAILABLE_VARIANTS.get(variant_key, PRODUCT_A)
