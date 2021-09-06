from django.contrib.auth.hashers import make_password
from rest_framework import serializers
import string, random
from .models import User


def generate_random_password():
    possibles = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(possibles) for i in range(64))

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        #fields = ('id', 'email', 'password', 'first_name', 'last_name', 'username')
        extra_kwargs = {'password': {'write_only': True}}



    def create(self, validated_data):
        next_username = str(User.objects.last().id + 1 if User.objects.exists() else 1)
        password = make_password(generate_random_password())
        user = User.objects.create_user(next_username, validated_data['email'], password, first_name=validated_data['first_name'], last_name=validated_data['last_name'])

        return user
