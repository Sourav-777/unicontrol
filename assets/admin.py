from django.contrib import admin
from .models import Asset

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'os_type', 'ip_address', 'owner', 'compliance_status')
    search_fields = ('hostname', 'ip_address', 'owner')
