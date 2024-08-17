from django.contrib import admin

# Register your models here.
@admin.register("user")
class TakeAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()
    search_fields = ()