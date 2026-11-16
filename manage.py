#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medispl_unemi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("No se pudo importar Django. Verifique que esté instalado en el entorno virtual.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
