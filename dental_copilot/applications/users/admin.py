from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    # add_form = UserCreationForm
    list_display = ('email','username','nombres','apellidos','genero', 'is_staff', 'is_active')
    ordering = ("email",)
    list_filter = ('is_staff',)
    
    fieldsets = (
        (None, {'fields': ('username','email', 'password', 'nombres', 'apellidos','genero', 'is_staff', 'is_active','is_admin')}),
    )
    add_fieldsets = (   
        (None, {'fields': ('username','email', 'password', 'password2', 'nombres', 'apellidos','genero', 'is_staff')}),
    )

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)