from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Arbitre)
admin.site.register(MatchCard)
admin.site.register(OrderArbitreMatch)
admin.site.register(OrderArbiterMatchInvite)

