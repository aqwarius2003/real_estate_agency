from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'new_building', 'owner')
    search_fields = ['town', 'address', 'owner']  # Поля для поиска: город, адрес, имя владельца
    readonly_fields = ['created_at']
    list_editable = ('new_building',)
    list_filter = ('new_building',)
admin.site.register(Flat, FlatAdmin)
