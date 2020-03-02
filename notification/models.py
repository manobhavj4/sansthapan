import random
import os
from django.db import models

from django.urls import reverse
# Create your models here.
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext	


def upload_image_path(instance, filename):
	#print(instance)
	#print(filename)
	new_filename = random.randint(1,3493492323)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "documents/{new_filename}/{final_filename}".format(new_filename= new_filename, final_filename = final_filename)


class Notification(models.Model):
	title		= models.CharField(max_length=120)
	slug		= models.SlugField(blank= True, unique= True)
	description	= models.TextField()
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):            #for object description in python3
		return self.title

	def __unicode__(self):        #for object description in python
		return self.title

	@property 
	def name(self):
		return self.title

class Gallery(models.Model):
	title		= models.CharField(max_length=120)
	image = models.ImageField(upload_to='images/')
	slug		= models.SlugField(blank= True, unique= True)
	uploaded_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):            #for object description in python3
		return self.title

	def __unicode__(self):        #for object description in python
		return self.title

	@property 
	def name(self):
		return self.title
