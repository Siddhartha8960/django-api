from django.urls import path , include
from . import views
from rest_framework import routers
from users.views import getUser,addUser,getUserById,updateUser,deleteUser


router = routers.DefaultRouter()
# router.register('Users',views.UserView)

urlpatterns = [
    path('getUsers',getUser),
    path('addUsers',addUser),
    path('getUserById/<id>',getUserById),
    path('updateUser/<id>',updateUser),
    path('deleteUser/<id>',deleteUser)
]
