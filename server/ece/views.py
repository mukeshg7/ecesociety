from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class FacultyList(generics.ListCreateAPIView):
	queryset=Faculty.objects.all()
	serializer_class=FacultySerializers

class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers

class NoticeList(generics.ListCreateAPIView):
	queryset=Notice.objects.all()
	serializer_class=NoticeSerializers

class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Notice.objects.all()
	serializer_class=NoticeSerializers

class MemberList(generics.ListCreateAPIView):
	queryset=Members.objects.all()
	serializer_class=MemberSerializers

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Members.objects.all()
	serializer_class=MemberSerializers




