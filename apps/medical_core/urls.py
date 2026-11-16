from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_atenciones, name='dashboard_atenciones'),
]
