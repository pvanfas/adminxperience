from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

app_name = "adminxperience"

urlpatterns = []


config = settings.ADMINXPERIENCE_CONFIG

admin.site.site_header = config.get("site_header", _("Django Control Panel"))
admin.site.site_title = config.get("site_title", _("Django Control Panel"))
admin.site.index_title = config.get("index_title", _("Welcome to Django Control Panel"))