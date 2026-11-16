from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('alertas/', views.panel_alertas, name='panel_alertas'),
]
