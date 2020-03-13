from rest_framework import serializers
from .models import Book,BookNumber


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        feilds=['id','isbn_10','isbn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        feilds=['id','name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookNumber
        feilds=['id','name','surname']

class BookSerializer(serializers.ModelSerializer):
    number=BookNumberSerializer(many=False)
    characters=BookNumberSerializer(many=True)
    authors=BookNumberSerializer(many=True)
    class Meta:
        model=Book
        feilds=['title','description','price','published','is_published','number','characters','authors']
