from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from rest_framework import generics

from books import models
from . import serializers


class ListBooks(generics.ListCreateAPIView):
	# permission_classes = permissions.AllowAny()
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    # def post(self, request, format=None):

    # 	return HttpResponse('ok')


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

