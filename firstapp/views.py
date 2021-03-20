from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework import generics
# Create your views here.

"""create a student and view list of students"""
class StudentLC(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

""""get a perticular student, can update and delete student"""
class StudentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer