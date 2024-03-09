from django.conf import settings

def main_context(request):
    return {
        'config': settings.ADMINXPERIENCE_CONFIG,
        'background': settings.ADMINXPERIENCE_CONFIG.get('background', '/static/adminxperience/img/background.jpg'),
    }
