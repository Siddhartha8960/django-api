from django.urls import path , include
from . import views
from rest_framework import routers
from blog.views import addBlog,getBlog


router = routers.DefaultRouter()


urlpatterns = [
    path('getBlog',getBlog),
    path('addBlog',addBlog),
]
