from rest_framework import serializers
from account.models import User
from club.models import *
from .models import *
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response

class ClubeSerializer(serializers.ModelSerializer):
    capitan = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Clube
        fields = ['name','capitan','active','logo']