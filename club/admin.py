from django.contrib import admin
from .models import *

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    model=Clube
    list_display=('capitan','name','active')

admin.site.register(Capitan)
admin.site.register(StadiumOwner)
admin.site.register(Player)
admin.site.register(Clube,ClubAdmin)
admin.site.register(Stadium)
admin.site.register(Match)
admin.site.register(GoalMatch)
