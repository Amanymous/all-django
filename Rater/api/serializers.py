from rest_framework import serializers
from .models import Todo,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=('id','title','name','amount','description','no_of_ratings','avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id','stars','user','todo')
# isky bad jitna kam is ma kiya ha wo view.py ma batana parega
# or is kam ko api/urls.py ki ma register karingy