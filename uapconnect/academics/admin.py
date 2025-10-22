from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, ClassRoutine, Mark

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title')

@admin.register(ClassRoutine)
class ClassRoutineAdmin(admin.ModelAdmin):
    list_display = ('course', 'day', 'time', 'room')

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'ct1', 'ct2', 'mid', 'final')