from django.contrib import admin
from .models import *

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    model=Clube
    list_display=('capitan','name','active')
class ClubPlayerAdmin(admin.ModelAdmin):
    model=ClubePlayer
    list_display=('player','clube','position','goals')

admin.site.register(Capitan)
admin.site.register(StadiumOwner)
admin.site.register(Player)
admin.site.register(ClubePlayer)
admin.site.register(Clube,ClubAdmin)
admin.site.register(Stadium)
admin.site.register(Match)
admin.site.register(GoalMatch)
