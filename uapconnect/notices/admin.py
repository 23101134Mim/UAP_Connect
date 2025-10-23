from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NoticeCategory, Notice

@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'posted_at')
