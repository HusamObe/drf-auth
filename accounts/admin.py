from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('User Information',{'fields' : ('username','email', 'password1','password2')}),
        ('personal information',{'fields': ('first_name','last_name','phone_number')})
    )


admin.site.register(CustomUser,CustomUserAdmin)