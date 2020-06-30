from rest_framework import serializers
from .models import *


class FacultySerializers(serializers.ModelSerializer):
	class Meta:
		model= Faculty

		fields=['id', 'name', 'image', 'email', 'phone']

class NoticeSerializers(serializers.ModelSerializer):
	class Meta:
		model= Notice

		fields=['id','title','description','date_time']

class MemberSerializers(serializers.ModelSerializer):
	class Meta:
		model=Members

		fields=['id','name','image','email','phone','fb','ln','yr']