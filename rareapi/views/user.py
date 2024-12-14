from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User

class UserView(ViewSet):
  
  def retrieve(self, request, pk):
    # Handle GET requests for single user
    try:
      user = User.objects.get(pk=pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)
    except User.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
  # Handle GET requests to get all users
    users = User.objects.all()
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    # Handle POST operations
    user = User.objects.create(
      first_name=request.data["first_name"],
      last_name=request.data["last_name"],
      bio=request.data["bio"],
      profile_image_url=request.data["profile_image_url"],
      email=request.data["email"],
      created_on=request.data["created_on"],
      active=request.data["active"],
      is_staff=request.data["is_staff"],
      uid=request.data["uid"]
    )
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    # Handle PUT requests for a user
    id = pk
    user = User.objects.get(pk=pk)
    user.first_name=request.data["first_name"]
    user.last_name=request.data["last_name"]
    user.bio=request.data["bio"]
    user.profile_image_url=request.data["profile_image_url"]
    user.email=request.data["email"]
    user.created_on=request.data["created_on"]
    user.active=request.data["active"]
    user.is_staff=request.data["is_staff"]
    user.uid=request.data["uid"]
    
    user.save()
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class UserSerializer(serializers.ModelSerializer):
  # JSON serializer for users
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')
    depth = 1
