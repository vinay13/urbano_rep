from django.db import models


class Vendor(models.Model):
	fname=models.CharField(max_length=128,default='firstname')
	lname=models.CharField(max_length=128,default='lastname')
	profile=models.CharField(max_length=128,default='plumber')
	gender=models.CharField(max_length=128,default='M')
	DOB=models.CharField(max_length=128,default='12-4-1979')
	state=models.CharField(max_length=128,default='MP')
	city=models.CharField(max_length=128,default='jbp')
	address=models.CharField(max_length=128,default='address')
	contactNo=models.IntegerField(default='+91')
	#Vendorimage=models.ImageField()


	def __str__(self):
		return self.fname






# Create your models here.
