from django.shortcuts import render
from .models import Student
# Create your views here.
from rest_framework import viewsets
from .serializers import StudentSerializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class= StudentSerializers