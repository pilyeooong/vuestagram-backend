from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('profile_image', 'gender', 'introduction')}),
    )
    list_display = ['id', 'username', 'email', 'profile_image', 'gender']


admin.site.register(User, UserAdmin)
