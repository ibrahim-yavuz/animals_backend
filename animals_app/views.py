from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AnimalSerializer
from .models import Animal

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all().order_by('animal_name')
    serializer_class = AnimalSerializer
