from django.db import models

class Customer(models.Model):
	id=models.AutoField(primary_key=True)
	fname=models.CharField(max_length=128,default='a')
	lname=models.CharField(max_length=128,default='b')
	DOB=models.CharField(max_length=128,default='c')
	contactno=models.IntegerField(default='+91')
	city=models.CharField(max_length=128,default='JBP')
	state=models.CharField(max_length=128,default='MP')
	landmark=models.CharField(max_length=128,default='e')
	address=models.CharField(max_length=128,default='f')
	pincode=models.IntegerField(default='288412')
#	CustomerImage=models.ImageField()

	def __str__(self):
		return self.fname +' '+ self.lname


# Create your models here.
