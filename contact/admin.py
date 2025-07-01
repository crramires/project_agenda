from django.contrib import admin
from .models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email',
    ordering = 'id',
    list_filter = 'created_date',
    search_fields = 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100


@admin.register(Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'id',
