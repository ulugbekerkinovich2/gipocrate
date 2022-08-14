from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

# Create your views here.

from basic_app import models, serializers


def index(request):
    return HttpResponse('Its working')

class Kasallik(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Болезни1.objects.all()
    serializer_class = serializers.Kasalliklar

class Kasalliklar(generics.ListCreateAPIView):
    queryset = models.Болезни1.objects.all()
    serializer_class = serializers.Kasalliklar

