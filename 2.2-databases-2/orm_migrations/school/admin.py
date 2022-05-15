from django.contrib import admin

from .models import Student, Teacher


class StudentTeacherInline(admin.TabularInline):
    model = Student.teacher.through
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentTeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentTeacherInline]