from django.contrib import admin

# Register your models here.
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as  _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 
from django.contrib.admin.sites import NotRegistered

user = get_user_model()
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = _('User Profile')

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    def get_readonly_fields(self, request, obj =None):
        django_readonly =  super().get_readonly_fields(request, obj)
        if obj:
            return django_readonly +('username',)
        return django_readonly


try:
    admin.site.unregister(user)
except NotRegistered:
    pass

admin.site.register(user,UserAdmin)