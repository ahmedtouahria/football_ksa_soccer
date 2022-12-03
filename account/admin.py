# admin.py
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
User = get_user_model()
class UserAdmin(BaseUserAdmin):
    list_display = ('id','username', 'phone','state','otp','count')
    list_filter = ('arbitre','stadium_owner' ,'admin','capitan' )
    fieldsets = (
        (None, {'fields': ('phone', 'password',)}),
        ('Personal info', {'fields': ('username', 'state',)}),
        ('Permissions', {'fields': ('admin','arbitre','stadium_owner','capitan')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    search_fields = ('phone','username')
    ordering = ('phone','username')
    filter_horizontal = ()
def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)
admin.site.register(User, UserAdmin)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
# Register onthersmodels