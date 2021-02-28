from django.db import models

# Create your models here.



class Param(models.Model):
	param_name = models.CharField(max_length=250, null=True,blank=True)
	content = models.TextField(max_length=1000, null=True,blank=True)
	image  = models.ImageField(upload_to='' , blank=True )
	activ = models.BooleanField(default=True)
	def __str__(self):
		return self.param_name 


class Service(models.Model):
	title = models.CharField(max_length=250, null=True,blank=True)
	description = models.CharField(max_length=250, null=True,blank=True)
	icon = models.CharField(max_length=250, null=True,blank=True)
	url = models.CharField(max_length=250, null=True,blank=True)
	activ = models.BooleanField(default=True)

	def __str__(self):
		return self.title 

class ProjectCategory(models.Model):
	title = models.CharField(max_length=250, null=True,blank=True)
	datarel = models.CharField(max_length=250, null=True,blank=True)
	activ = models.BooleanField(default=True)

	def __str__(self):
		return self.title 

class Project(models.Model):
	title = models.CharField(max_length=250, null=True,blank=True)
	image  = models.ImageField(upload_to='' , blank=True )
	url = models.CharField(max_length=250, null=True,blank=True)
	projectcategory  = models.ForeignKey(ProjectCategory , on_delete=models.SET_NULL,  null = True, blank=True)
	activ = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title 
