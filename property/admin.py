from django.contrib import admin

from .models import Flat, Complaint


class ComplaintInline(admin.TabularInline):
    model = Complaint
    extra = 0

class Meta:
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'

class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'new_building', 'owner')
    search_fields = ['town', 'address', 'owner']  # Поля для поиска: город, адрес, имя владельца
    readonly_fields = ['created_at']
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    inlines = [ComplaintInline]


admin.site.register(Flat, FlatAdmin)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('flat',)  # Добавляем raw_id_fields для поля ForeignKey flat
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'


# admin.site.register(Complaint, ComplaintAdmin)
