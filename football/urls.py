from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from landing.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/',include("account.urls")),
    path('api/arbitre/',include("arbitre.urls")),
    path('api/stadium/',include("stadium.urls")),
    path('api/clube/',include("club.urls")),
    path('',home)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)