import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webcrm.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('jose', 'carlos213244@gmail.com', 'carlos2306')
    print("Superusuario creado")
else:
    print("Superusuario ya existe")
