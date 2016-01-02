from django.db import models


class JobDetails(models.Model):
	id=models.AutoField(primary_key=True)
	customer_name=models.CharField(max_length=128,default='narendrasir')
	createdateTime=models.CharField(max_length=128,default='cat')
	WantedDate=models.CharField(max_length=128,default='cat')
	Wantedtimestart=models.CharField(max_length=128,default='cat')
	category_name=models.CharField(max_length=128,default='cat')
	subcategory_name=models.CharField(max_length=128,default='subc')
	status=models.CharField(max_length=128,default='done/pending/canceled')
	description=models.CharField(max_length=128,default='describe')
  #  jobcreate_dateTime=models.datetime()
  #  jobWantedDate=models.datetime()
  #  jobWantedtimestart=models.CharField(max_length=128,default='wed 10:10')
  #  jobImage=models.ImageField()

	def __str__(self):
		return self.status



class JobAssign(models.Model):
	id=models.AutoField(primary_key=True)
	jobid=models.CharField(max_length=128,default='0')
	vendorid=models.CharField(max_length=128,default='0')
	vendorname=models.CharField(max_length=128,default='n')
	datetime=models.CharField(max_length=128,default='20-01-2015')
	payment=models.CharField(max_length=128,default='not paid')
	status=models.CharField(max_length=128,default='pending')
	


	def __str__(self):
		return self.status





#class job_list():




#class job_assignment(): 


# Create your models here.
