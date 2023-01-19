from django.contrib import admin
from .models import Employee

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name', 'last_name')
    # para datos tipo date
    # date_hierarchy = 'discount_until'


admin.site.register(Employee, ProductAdmin)
