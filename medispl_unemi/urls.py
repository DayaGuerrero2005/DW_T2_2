# medispl_unemi/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('usuarios/', include('apps.users.urls')),
    path('archivos/', include('apps.file_manager.urls')),
    path('', include('apps.medical_core.urls')),
]

# Puntos de variación en el enrutador principal mediante include() condicional
if getattr(settings, 'ENABLE_REPORTS', False):
    urlpatterns.append(
        path('reportes/', include(('apps.reports.urls', 'reports'), namespace='reports'))
    )

if getattr(settings, 'ENABLE_NOTIFICATIONS', False):
    urlpatterns.append(
        path('notificaciones/', include(('apps.notifications.urls', 'notifications'), namespace='notifications'))
    )
