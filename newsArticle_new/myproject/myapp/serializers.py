from dataclasses import field, fields
from rest_framework import serializers
from myapp.models import NewsArticles,Like, User, Locality, City

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name','contact','city','is_author','is_user','is_admin')

class NewsArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticles
        fields = ('user_id','headline','title','mainbody','author','locality','like','comment','tags')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('news_id','user_id')

class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'