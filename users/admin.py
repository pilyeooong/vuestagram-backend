from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

class UserAdmin(BaseUserAdmin):
    model = User
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('profile_image', 'gender', 'introduction')}),
    )
    list_display = ["username", "email", "profile_image", "gender"]

admin.site.register(User, UserAdmin)