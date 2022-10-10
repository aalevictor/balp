from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'twitch', 'name')
    search_fields = ['twitch']
    filter_horizontal = ()
    lits_filter = ()
    ordering = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)
