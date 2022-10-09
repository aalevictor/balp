from django.contrib import admin

from bal.models import Bal, Club, Goalkeeper, Player, Technical

# Register your models here.

admin.site.register(Player)
admin.site.register(Technical)
admin.site.register(Goalkeeper)
admin.site.register(Bal)
admin.site.register(Club)
