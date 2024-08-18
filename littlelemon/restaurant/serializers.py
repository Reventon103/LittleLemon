from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class MenuSerializer(ModelSerializer):
    pass

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']