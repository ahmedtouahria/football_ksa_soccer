from django.urls import path,include
from account.views import *
from rest_framework import routers
from knox.views import LogoutView


router = routers.DefaultRouter()
router.register(r'register', RegisterView, basename='task')


urlpatterns = [ 
    path('',include(router.urls)),# هنا يحدث التسجيل الأولي للمستخدم  
    path('login/', LoginView.as_view(), name='knox_logout'),# login user
    path('send_phone/',ValidatePhoneSendOTP.as_view(),name='get-login-otp-mobile'),#  هنا يحط رقم الهاتف برك باه نرسلولو رمز
    path('verify_otp/',VerifyPhoneOTPView.as_view(),name='login-otp-verify'), # هنا يتم التحقق من الرمز
    path('logout/', LogoutView.as_view(), name='knox_logout')
]

