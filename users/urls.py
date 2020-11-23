from django.urls import path , include
from . import views
from rest_framework import routers
from users.views import getUser,addUser,getUserById,updateUser,deleteUser


router = routers.DefaultRouter()
# router.register('Users',views.UserView)

urlpatterns = [
    path('users/getUsers',getUser),
    path('users/addUsers',addUser),
    path('users/getUserById/<id>',getUserById),
    path('users/updateUser/<id>',updateUser),
    path('users/deleteUser/<id>',deleteUser)
]
