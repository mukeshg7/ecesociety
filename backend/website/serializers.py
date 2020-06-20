from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class FacultySerializers(serializers.ModelSerializer):
	class Meta:
		model= Faculty

		fields=['id', 'first_name', 'last_name', 'image', 'email', 'phone']

class MembersSerializers(serializers.ModelSerializer):
	class Meta:
		model= Members

		fields=['id', 'first_name', 'last_name', 'year', 'image', 'email', 'fb', 'phone']

class NoticeSerializers(serializers.ModelSerializer):
	class Meta:
		model= Notice

		fields=['title','description','date_time']
