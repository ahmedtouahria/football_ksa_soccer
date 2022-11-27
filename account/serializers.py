from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "phone","state","image","arbitre",'stadium_owner']
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {"required": True},
            "state": {"required": True},
            "password": {"required": True},
            "phone": {"required": True},
            "arbitre": {"required": True},
            "stadium_owner": {"required": True},
        }
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
class AuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        if phone and password:
            user = authenticate(request=self.context.get('request'),
                                phone=phone, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "phone" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
        