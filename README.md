# MediSPL-UNEMI: Línea de Productos de Software en Django

Proyecto desarrollado para la **Práctica 4** de la asignatura **Gestión de la Configuración de Software (GESCONSOF)** en la **Universidad Estatal de Milagro (UNEMI)**.

## Arquitectura de Variabilidad (SPL)
El sistema implementa una Línea de Productos de Software (SPL) para la gestión de atenciones médicas y triaje institucional, permitiendo derivar dos variantes operativas mediante puntos de variación controlados en `config_product.py`:

- **Variante A (`PRODUCT_A` - Sistema Básico):** Incluye únicamente los activos del núcleo (`authentication`, `users`, `medical_core`, `file_manager`) con `ENABLE_REPORTS = False` y `ENABLE_NOTIFICATIONS = False`.
- **Variante B (`PRODUCT_B` - Sistema Completo):** Activa los módulos extendidos de exportación de reportes clínicos (`reports`) y alertas en tiempo real (`notifications`) con `ENABLE_REPORTS = True` y `ENABLE_NOTIFICATIONS = True`.

## Cómo cambiar de variante
1. Edite `medispl_unemi/config_product.py` o defina la variable de entorno `ACTIVE_PRODUCT_VARIANT`:
   ```bash
   export ACTIVE_PRODUCT_VARIANT=PRODUCT_A  # Para Variante A (Básica)
   export ACTIVE_PRODUCT_VARIANT=PRODUCT_B  # Para Variante B (Completa)
   ```
2. Ejecute el servidor de desarrollo:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
