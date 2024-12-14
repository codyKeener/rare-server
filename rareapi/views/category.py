"""View module for handling requests about types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):
    """ types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single type
        
        Returns:
            Response -- JSON serialized type
        """
        try:
            category = Category.objects.get(pk=pk)
            serializer = SingleCategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized instance
        """
        category = Category.objects.create(
        label=request.data["label"],
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a genre

        Returns:
            Response -- Empty body with 204 status code
        """

        id = pk
        category = Category.objects.get(pk=pk)
        category.label = request.data["label"]

        category.save()

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'label')
        depth = 1

class SingleCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = ('id', 'label')
            depth = 1
