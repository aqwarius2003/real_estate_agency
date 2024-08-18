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


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner',)
    extra = 0
    verbose_name = 'Владелец'
    verbose_name_plural = 'Владельцы'


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('town', 'address', 'new_building', 'likes_count')
    search_fields = ['town', 'address']  # Поля для поиска: город, адрес
    readonly_fields = ['created_at', 'likes_count']
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    inlines = [ComplaintInline, LikeInline, OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('flat',)  # raw_id_fields для поля ForeignKey flat
    verbose_name = 'Жалоба'
    verbose_name_plural = 'Жалобы'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    # list_display = ('user', 'flat')
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone')
    raw_id_fields = ('flat',)
