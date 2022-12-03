from django.shortcuts import render
from constance import config
from .models import *
from account.models import User
from club.models import Player , Clube
# Create your views here.
def home(request):
    feutures = Feuture.objects.all()
    images = ScreenShot.objects.all()
    number_of_users = User.objects.all().count()
    number_of_players = Player.objects.all().count()
    number_of_clubs = Clube.objects.all().count()
    feedbacks= FeedBack.objects.all()
    context={
    "config":config,
    "feutures":feutures,
    "images":images,
    "number_of_users":number_of_users,
    "number_of_players":number_of_players,
    "number_of_clubs":number_of_clubs,
    "feedbacks":feedbacks,
    }
    return render(request,"index.html",context)