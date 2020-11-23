from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.models import Blog
from response import responseHandler,errorHandler
from bson import ObjectId


@api_view(['GET'])
def getBlog(request):
    try:
        blog = Blog.objects.all()
        serial = BlogSerializer(blog, many=True)
        res={
            "message":"Blog List",
            "result":serial.data
        }
        return responseHandler(res)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def addBlog(request):
    try:
        blog_serializer = BlogSerializer(data=request.data)
        if(blog_serializer.is_valid()):
            blog_serializer.create(request.data)
            res={
                "message":"Blog added successfully",
                "result":blog_serializer.data
                }
            return responseHandler(res)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)        
