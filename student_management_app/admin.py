from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, AdminHOD, Staff, Student


class UserAdmin(BaseUserAdmin):

    list_display = ["email", "name", "user_type", "is_admin", "is_active", "updated_at"]

    list_filter = ["is_admin", "user_type", "is_active"]
    fieldsets = [
        ('User Details', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "user_type"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            "Create an Account",
            {
                "classes": ["wide"],
                "fields": ["email", "name", "is_admin", 
                        #    "userContact", "userOrganization", 
                           "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)


admin.site.register(AdminHOD)
admin.site.register(Staff)
admin.site.register(Student)


