import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')  # Cambia 'crm' por tu nombre de proyecto
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('jose', 'carlos213244@gmail.com', 'carlos2306')
