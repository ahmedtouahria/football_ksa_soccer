from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from account.functions import send_otp
from account.serializers import RegisterSerializer
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions, status
from .permissions import *
from django.utils.translation import gettext_lazy as _
User = get_user_model()

# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes= (IsOwnerOrReadOnly,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.data.get("arbitre") == request.data.get("stadium_owner"):
            return Response({"success":False,"message":_("user cannot be arbitre and stadium owner")},status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'response': serializer.data,
            'success': True,
            'message': 'User created successfully',
            'status': status.HTTP_201_CREATED,

        })

class ValidatePhoneSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            phone_number = request.data.get('phone',None)
            if phone_number:
                phone = str(phone_number)
                user = User.objects.filter(phone__iexact=phone)
                if user.exists():
                    user_data = user.first()
                    new_otp = send_otp(phone)
                    user_data.otp = new_otp
                    print("new otp",new_otp)
                    user_data.save()
                    return Response({
                        'message': _('OTP sent successfully'),
                        'status': status.HTTP_200_OK,
                    })
                else:
                    return Response({
                        'message': _('User not found ! please register'),
                        'status': status.HTTP_404_NOT_FOUND,
                    }
                    )
            else:
                return Response({
                    'message': _('Phone number is required'),
                    'status': status.HTTP_400_BAD_REQUEST,
                })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })


# verify otp
class VerifyPhoneOTPView(APIView):
    def post(self, request, format=None):
        try:
            phone = request.data.get('phone')
            otp = request.data.get('otp')
            print(phone, otp)

            if phone and otp:
                user = User.objects.filter(phone__iexact=phone)
                if user.exists():
                    user = user.first()
                    if user.otp == otp:
                        login(request, user)
                        return Response({
                            'status': True,
                            'details': 'Login Successfully',
                            'token': AuthToken.objects.create(user)[1],
                            'response': {
                                'id': user.id,
                                'username': user.username,
                                'phone': user.phone,
                                'state': user.state,
                            }})
                    else:
                        return Response({'message': _('OTP does not match')}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': _('User does not exist')}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': _('Phone or OTP is missing')}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': str(e),
                'details': 'Login Failed'
            })


# logout api view
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format=None):
        try:
            request.user.auth_token.delete()
            return Response({
                'message': 'Logout successfully',
                'status': status.HTTP_200_OK,
            })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })