from rest_framework import serializers
from .models import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '_id','blog_name','created',