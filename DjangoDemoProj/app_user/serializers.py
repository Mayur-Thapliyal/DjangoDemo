from rest_framework import serializers
from app_user.models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model  = UserModel
        extra_kwargs = {
            'password': {'write_only': True}
        }