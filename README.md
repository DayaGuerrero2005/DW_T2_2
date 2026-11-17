# MediSPL-UNEMI: Línea de Productos de Software en Django

Proyecto desarrollado para la **Práctica 4** (`G004-S13-SOFTWARE2019-PRESENCIAL-GESTIÓN DE LA CONFIGURACIÓN DE SOFTWARE-B1`) de la asignatura **Gestión de la Configuración de Software (GESCONSOF)** en la **Universidad Estatal de Milagro (UNEMI)**.

## Datos Académicos
- **Facultad:** Facultad de Ciencias e Ingeniería (FACI)
- **Carrera:** Ingeniería en Software (Modalidad Presencial)
- **Asignatura:** Gestión de la Configuración de Software
- **Docente:** Msg. Oviedo Armijos Omar Andrés
- **Periodo Académico:** Agosto 2026 a Diciembre 2026
- **Fecha de Entrega:** Viernes, 20 de noviembre de 2026

## Autores del Grupo
1. **Eduardo Javier Quinteros Pacheco** — *Sesión 1: Identificación de componentes reutilizables*
2. **Gleyder Julissa Lescano Paredes** — *Sesión 2: Modularización y separación de variantes*
3. **Dayanara Rosario Guerrero Jara** — *Sesión 3: Configuración de variabilidad*
4. **Kevin Ernesto Barboza Cargua** — *Sesión 4: Documentación y línea de productos*

---

## Arquitectura de Variabilidad (SPL)
El sistema implementa una Línea de Productos de Software (SPL) para la gestión de atenciones médicas y triaje institucional, permitiendo derivar variantes operativas mediante puntos de variación controlados en `medispl_unemi/config_product.py`, `medispl_unemi/settings.py` y enrutamiento condicional `include()` en `medispl_unemi/urls.py`:

### 1. Activos Base (`CORE_APPS` - Comunalidad 100%)
- `apps.authentication`: Autenticación de usuarios y seguridad de sesión.
- `apps.users`: Gestión de usuarios y roles RBAC.
- `apps.file_manager`: Carga y validación de soportes digitales clínicos.
- `apps.medical_core`: Núcleo del dominio médico y registro de triaje Manchester.

### 2. Activos Opcionales (`OPTIONAL_APPS` - Variabilidad Funcional)
- `apps.reports` (`ENABLE_REPORTS`): Exportación de reportes clínicos en PDF y CSV.
- `apps.notifications` (`ENABLE_NOTIFICATIONS`): Alertas clínicas activas en tiempo real.
- Filtro Multicriterio (`ENABLE_ADVANCED_SEARCH`): Búsqueda combinada por paciente, código de ficha y nivel de triaje.

### 3. Variantes Definidas en `config_product.py`
- **Variante A (`PRODUCT_A` - Sistema Básico):** Incluye únicamente los activos del núcleo (`ENABLE_REPORTS = False`, `ENABLE_NOTIFICATIONS = False`, `ENABLE_ADVANCED_SEARCH = False`).
- **Variante B (`PRODUCT_B` - Sistema Completo Extendido):** Activa los módulos extendidos de exportación de reportes clínicos (`reports`), alertas en tiempo real (`notifications`) y búsqueda avanzada (`ENABLE_REPORTS = True`, `ENABLE_NOTIFICATIONS = True`, `ENABLE_ADVANCED_SEARCH = True`).

---

## Instrucciones de Ejecución

### Ejecutar Variante A (Sistema Básico)
```powershell
$env:ACTIVE_PRODUCT_VARIANT="PRODUCT_A"
python manage.py migrate
python manage.py runserver 8000
```

### Ejecutar Variante B (Sistema Completo Extendido)
```powershell
$env:ACTIVE_PRODUCT_VARIANT="PRODUCT_B"
python manage.py migrate
python manage.py runserver 8000
```

### Probar Aislamiento de `ENABLE_REPORTS` (Sesión 2)
```powershell
# Con ENABLE_REPORTS = False
$env:ACTIVE_PRODUCT_VARIANT="PRODUCT_A"
$env:ENABLE_REPORTS_OVERRIDE="False"
python manage.py runserver 8000

# Con ENABLE_REPORTS = True (solo reportes activos)
$env:ACTIVE_PRODUCT_VARIANT="PRODUCT_A"
$env:ENABLE_REPORTS_OVERRIDE="True"
python manage.py runserver 8000
```
