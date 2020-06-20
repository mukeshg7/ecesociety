from django.db import models
from django.utils import timezone



class Faculty(models.Model):
	first_name=models.CharField(max_length=50 , null=False)
	last_name=models.CharField(max_length=50, null=False)
	image=models.ImageField(upload_to='faculty_images', default='default.jpg')
	email=models.EmailField(null=True, blank=True)
	phone=models.CharField(null=True, blank=False, max_length=15)

	def __str__(self):
		return (self.first_name+self.last_name)
    


class Members(models.Model):
	yr_choices = [
        (1,'First Year'),
        (2,'Second Year'),
        (3,'Third Year'),
        (4,'Final Year'),
    ]
	first_name=models.CharField(max_length=50 , null=False)
	last_name=models.CharField(max_length=50, null=False)
	image=models.ImageField(upload_to='member_images', default='default.jpg')
	year=models.IntegerField(choices= yr_choices, default=2)
	fb=models.URLField(null=True, blank=True)
	email=models.EmailField(null=True,blank=True)
	phone=models.CharField(null=True, blank=False, max_length=15)

	def __str__(self):
		return (self.first_name+self.last_name)


class Notice(models.Model):
	title=models.CharField(max_length=50, null=False)
	description=models.TextField(max_length=100)
	date_time=models.DateField(null=True, blank=True)

	def __str__(self):
		return self.title
    
