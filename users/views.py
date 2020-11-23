from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from response import responseHandler,errorHandler
from bson import ObjectId

# Create your views here.


# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


@api_view(['GET'])
def getUser(request):
    try:
        user = User.objects.all()
        serial = UserSerializer(user, many=True)
        res={
            "message":"Users List",
            "result":serial.data
        }
        return responseHandler(res)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def addUser(request):
    try:
        user_serializer = UserSerializer(data=request.data)
        if(user_serializer.is_valid()):
            user_serializer.create(request.data)
            res={
                "message":"User added successfully",
                "result":user_serializer.data
                }
            return responseHandler(res)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)        


@api_view(['GET'])
def getUserById(request, id):
    try:
        id = ObjectId(id)
        user = User.objects.get(_id=id)
        serial = UserSerializer(user, many=False)
        res={
            "message":"User found successfully",
            "result":serial.data
            }
        return responseHandler(res)
    except User.DoesNotExist:
        res={"message":'User Does not Exists'}
        return errorHandler(res)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['PUT'])
def updateUser(request, id):
    try:
        _id = ObjectId(id)
        user = User.objects.get(pk=_id)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            res={
            "message":"User updated successfully",
            "result":user_serializer.data
            }
            return responseHandler(res)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        res={"message":'User Does not Exists'}
        return errorHandler(res)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        _id = ObjectId(id)
        user = User.objects.get(pk=_id)
        user.delete()
        res={"message":"User deleted successfully"}
        return responseHandler(res)
    except User.DoesNotExist:
        res={"message":'User Does not Exists'}
        return errorHandler(res)
    except Exception as e:
        return Response(str(e), status = status.HTTP_500_INTERNAL_SERVER_ERROR)        