from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","company_name","age","city","state","zip","email","web"]