from django.db import models

class Faculty(models.Model):
	name=models.CharField(max_length=50 , null=False)
	#last_name=models.CharField(max_length=50, null=False)
	image=models.ImageField(upload_to='faculty_images', default='default.jpg')
	email=models.EmailField(null=True, blank=True)
	phone=models.CharField(null=True, blank=False, max_length=15)

	def __str__(self):
		return (self.name)

class Notice(models.Model):
	title=models.CharField(max_length=50, null=False)
	description=models.TextField(max_length=100)
	date_time=models.DateField(null=True, blank=True)

	def __str__(self):
		return self.title

class Members(models.Model):
	name=models.CharField(max_length=50, null= False)
	image=models.ImageField(upload_to='member_images', default='default.jpg')
	email=models.EmailField(null=True, blank=True)
	phone=models.CharField(null=True,blank=False, max_length=15)
	fb=models.URLField(null=True, blank=False)
	ln=models.URLField(null=True, blank=False)
	yr=models.IntegerField(null=True, blank=False)
