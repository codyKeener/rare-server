from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag, Tag, Post

class PostTagView(ViewSet):
  
  def retrieve(self, request, pk):
    # Handle GET requests for single postTag
    try:
      postTag = PostTag.objects.get(pk=pk)
      serializer = PostTagSerializer(postTag)
      return Response(serializer.data)
    except PostTag.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
  # Handle GET requests to get all postTags
    postTags = PostTag.objects.all()
    
    serializer = PostTagSerializer(postTags, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    # Handle POST operations
    postId = Post.objects.get(pk=request.data["post_id"])
    tagId = Tag.objects.get(pk=request.data["tag_id"])
    
    postTag = PostTag.objects.create(
      post_id=postId,
      tag_id=tagId,
    )
    serializer = PostTagSerializer(postTag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    # Handle PUT requests for a postTag
    postId = Post.objects.get(pk=request.data["post_id"])
    tagId = Tag.objects.get(pk=request.data["tag_id"])
    
    id = pk
    postTag = PostTag.objects.get(pk=pk)
    postTag.post_id = postId
    postTag.tag_id = tagId
    
    postTag.save()
    
    serializer = PostTagSerializer(postTag)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    postTag = PostTag.objects.get(pk=pk)
    postTag.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class PostTagSerializer(serializers.ModelSerializer):
  # JSON serializer for postTags
  class Meta:
    model = PostTag
    fields = ('id', 'post_id', 'tag_id')
    depth = 1
    