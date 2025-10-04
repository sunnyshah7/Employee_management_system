from django.http import JsonResponse
import os

def check_env(request):
    env_vars = {
        'DJANGO_DEBUG': os.environ.get('DJANGO_DEBUG', 'Not Set'),
        'PYTHON_VERSION': os.environ.get('PYTHON_VERSION', 'Not Set'),
        'DATABASE_URL': 'Set' if os.environ.get('DATABASE_URL') else 'Not Set',
        'DJANGO_SETTINGS_MODULE': os.environ.get('DJANGO_SETTINGS_MODULE', 'Not Set'),
    }
    return JsonResponse(env_vars)