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
  # Handle GET requests to get all comments
    
        comments = Comments.objects.all()
        
        postId = request.query_params.get('post_id', None)
        
        if postId is not None:
            comments = comments.filter(post_id=postId)
        
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
  
    def update(self, request, pk):
        # Handle PUT requests for a comment
        author_id = User.objects.get(uid=request.data["author_id"])
        post_Id = Post.objects.get(pk=request.data["post_id"])
    

        id = pk
        comment = Comments.objects.get(pk=pk)
        comment.post_id = post_Id
        comment.author_id = author_id
        comment.content=request.data["content"]
        comment.created_on=request.data["created_on"]
        comment.save()
        
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        comments = Comments.objects.get(pk=pk)
        comments.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
  
       
class CommentsSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comments
        fields = ('id', 'author_id', 'post_id', 'content', 'created_on')