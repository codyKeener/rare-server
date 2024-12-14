"""View module for handling requests about comments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comments, User, Post


class CommentsView(ViewSet):
    """Tuna Api Comments view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comments

        Returns:
            Response -- JSON serialized comments
        """
        comments = Comments.objects.get(pk=pk)
        serializer = CommentsSerializer(comments)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """
        
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
      
    def create(self, request):
      """Handle POST operations

      Returns
          Response -- JSON serialized game instance
      """
      author_id = User.objects.get(uid=request.data["author_id"])
      post_id = Post.objects.get(pk=request.data["post_id"])

      comment = Comments.objects.create(
          author_id=author_id,
          post_id=post_id,
          content=request.data["content"],
          created_on=request.data["created_on"],
      )
      serializer = CommentsSerializer(comment)
      return Response(serializer.data)  
       
class CommentsSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comments
        fields = ('id', 'author_id', 'post_id', 'conetent', 'created_on')