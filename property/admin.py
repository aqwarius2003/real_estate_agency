from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'owner')
    search_fields = ['town', 'address', 'owner']  # Поля для поиска: город, адрес, имя владельца
    readonly_fields = ['created_at']

admin.site.register(Flat, FlatAdmin)
