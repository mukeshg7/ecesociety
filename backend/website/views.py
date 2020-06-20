from .models import *
from .serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response

class FacultyList(generics.ListCreateAPIView):
	queryset= Faculty.objects.all()
	serializer_class=FacultySerializers

class MemberList(generics.ListCreateAPIView):
	queryset= Members.objects.all()
	serializer_class=MembersSerializers

class NoticeList(generics.ListCreateAPIView):
	queryset=Notice.objects.all()
	serializer_class=NoticeSerializers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'members': reverse('members-list', request=request, format=format),
        'faculty': reverse('faculty-list', request=request, format=format),
        'notice': reverse('notice-list', request=request, format=format),

    })