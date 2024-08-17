from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TakeAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "assigned_to")
    list_filter = ("status", "assigned_to")
    search_fields = ("title", "description")

'''
django-admin startproject myproject
cd myproject
python manage.py startapp tasks
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
'''