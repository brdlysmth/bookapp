from rest_framework import serializers
from books import models 

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		fields = ('id', 'title', 'book_author', 'summary')
		model = models.Post