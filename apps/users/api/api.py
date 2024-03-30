# rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# serializers
from apps.users.api.serializers import UserSerializer, UserListSerializer

#models
from apps.users.models import User


@api_view(['GET', 'POST'])
def user_api_view(request):

  if request.method == 'GET':
    users = User.objects.all().values('id', 'username', 'email', 'password')
    user_serializer = UserListSerializer(users, many=True)

    return Response(user_serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'POST':
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
      user_serializer.save()
      return Response(user_serializer.data)
    
    else:
      return Response(user_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
  # query set
  user = User.objects.filter(pk=pk).first()

  # validation
  if user:

      # retrive
      if request.method == 'GET':
          user_serializer = UserSerializer(user)
          return Response(user_serializer.data, status=status.HTTP_200_OK)
      
      # update
      elif request.method == 'PUT':
          user_serializer = UserSerializer(user, data=request.data)
          if user_serializer.is_valid():
             user_serializer.save()
             return Response(user_serializer.data, status=status.HTTP_200_OK)
          return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      # delete
      elif request.method == 'DELETE':
          user.delete()
          return Response(data=None, status=status.HTTP_204_NO_CONTENT)
  return Response({'message': 'user does not exists'}, status=status.HTTP_404_NOT_FOUND)
         
      

# class UserAPIView(APIView):
    
#     def get(self, request):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many=True)

#         return Response(user_serializer.data, status=status.HTTP_200_OK)



    

