from rest_framework import serializers
from common.models import UserModel
from djoser.serializers import UserSerializer


class BaseSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    deleted_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")


class BaseUserSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'first_name',
            'last_name',
            'email'
        )
