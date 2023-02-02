from django.contrib import admin
from .models import Role, Member
from django.contrib.auth.admin import UserAdmin


class MemberAdmin(UserAdmin):
    model = Member
    list_display = ('username', 'email', 'role',
                    'first_name', 'last_name', 'is_staff', 'role',)
    list_filter = ('username', 'email', 'role',
                   'first_name', 'last_name', 'is_staff', 'role',)
    fieldsets = (
        (None, {'fields': ('username', 'email',
                           'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role',
                       'first_name', 'last_name', 'is_staff', )}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Member, MemberAdmin)

# Register your models here.


admin.site.register(Role)
# admin.site.register(Member)
