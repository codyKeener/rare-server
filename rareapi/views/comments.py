"""View module for handling requests about comments"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comments


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
       
class CommentsSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comments
        fields = ('id', 'author_id', 'post_id', 'conetent', 'created_on')