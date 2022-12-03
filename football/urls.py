from django.contrib import admin
from django.urls import path , include
from landing.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/',include("account.urls")),
    path('api/arbitre/',include("arbitre.urls")),
    path('api/stadium/',include("stadium.urls")),
    path('api/clube/',include("club.urls")),
    path('',home)

]
