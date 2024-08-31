from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "password")
    list_filter = ("is_active", "is_staff", "groups")
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "password1", "password2")}),)

admin.site.register(User, CustomUserAdmin)