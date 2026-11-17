from django.test import TestCase, Client
from django.conf import settings

class MediSPLVariabilityTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dashboard_loads_successfully(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'MediSPL-UNEMI')
        self.assertContains(response, 'ATN-2026-0891')

    def test_core_endpoints_active(self):
        self.assertEqual(self.client.get('/auth/login/').status_code, 200)
        self.assertEqual(self.client.get('/usuarios/').status_code, 200)
        self.assertEqual(self.client.get('/archivos/upload/').status_code, 200)

    def test_optional_endpoints_match_configuration(self):
        if getattr(settings, 'ENABLE_REPORTS', False):
            self.assertEqual(self.client.get('/reportes/exportar/pdf/').status_code, 200)
            self.assertEqual(self.client.get('/reportes/exportar/csv/').status_code, 200)
        if getattr(settings, 'ENABLE_NOTIFICATIONS', False):
            self.assertEqual(self.client.get('/notificaciones/alertas/').status_code, 200)
