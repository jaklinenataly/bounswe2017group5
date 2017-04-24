from rest_framework import serializers
from apiApp.models import Post
 
# Create serializers here

 class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('id', 'text', 'author') # a field for comments is needed
