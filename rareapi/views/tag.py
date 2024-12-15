from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag, Post

class TagView(ViewSet):
  
  def retrieve(self, request, pk):
    # Handle GET requests for single tag
    try:
      tag = Tag.objects.get(pk=pk)
      posts = Post.objects.filter(tagposts__tag_id=tag)
      tag.posts=posts.all()
      serializer = SingleTagSerializer(tag)
      return Response(serializer.data)
    except Tag.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
  # Handle GET requests to get all tags
    tags = Tag.objects.all()
    
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    # Handle POST operations
    tag = Tag.objects.create(
      label=request.data["label"],
    )
    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    # Handle PUT requests for a tag
    id = pk
    tag = Tag.objects.get(pk=pk)
    tag.label = request.data["label"]
    
    tag.save()
    
    serializer = TagSerializer(tag)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    tag = Tag.objects.get(pk=pk)
    tag.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class TagSerializer(serializers.ModelSerializer):
  # JSON serializer for tags
  class Meta:
    model = Tag
    fields = ('id', 'label')
    depth = 1
    
class PostSerializer(serializers.ModelSerializer):
  # JSON serializer for posts
  class Meta:
    model = Post
    fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
    
class SingleTagSerializer(serializers.ModelSerializer):
  #JSON serializer for a single tag
  posts = PostSerializer(read_only=True, many=True)
  class Meta:
    model = Tag
    fields = ('id', 'label', 'posts')
    depth = 1
