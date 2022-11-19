from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "phone","state","image","arbitre",'stadium_owner']
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {"required": True},
            "state": {"required": True},
            "phone": {"required": True},
            "arbitre": {"required": True},
            "stadium_owner": {"required": True},
        }
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
