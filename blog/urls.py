from django.urls import path , include
from . import views
from rest_framework import routers
from blog.views import addBlog,getBlog


router = routers.DefaultRouter()


urlpatterns = [
    path('blog/getBlog',getBlog),
    path('blog/addBlog',addBlog),
    # path('users/getUserById/<id>',getUserById),
    # path('users/updateUser/<id>',updateUser),
    # path('users/deleteUser/<id>',deleteUser)
]
