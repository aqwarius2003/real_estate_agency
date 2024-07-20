from django.contrib import admin

from .models import Flat, Complaint, Like, Owner


class ComplaintInline(admin.TabularInline):
    model = Complaint
    extra = 0


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
    verbose_name_plural = 'Лайки'


class Meta:
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'new_building', 'owner', 'owners_phonenumber', 'owner_pure_phone', 'likes_count')
    search_fields = ['town', 'address', 'owner']  # Поля для поиска: город, адрес, имя владельца
    readonly_fields = ['created_at', 'likes_count']
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    inlines = [ComplaintInline, LikeInline]


# admin.site.register(Flat, FlatAdmin)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('flat',)  # raw_id_fields для поля ForeignKey flat
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'


# admin.site.register(Complaint, ComplaintAdmin)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # list_display = ('user', 'flat')
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone')
    raw_id_fields = ('flat',)
