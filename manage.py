#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Tidak dapat mengimpor Django. Apakah Anda yakin itu telah tersedia di PYTHONPATH Anda?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
