from django.db import models
from random import randint
from vendor.models import Vendor
from category.models import Category,SubCategory
from customer.models import Customer
class JobDetailsManager(models.Manager):
	def status_pending_count(self):
		return self.filter(status = 'pending').count()
	
	def status_done_count(self):
		return self.filter(status = 'done').count()	


class JobDetails(models.Model):
	id=models.AutoField(primary_key=True)
	customer_id=models.ForeignKey(Customer,null=True,blank=True)
	#customer_name=models.CharField(max_length=128,default='narendrasir')
	createdateTime=models.DateField(auto_now=False, auto_now_add=False)
	WantedDate=models.DateField(auto_now=False, auto_now_add=False)
	Wantedtimestart=models.DateField(auto_now=False, auto_now_add=False)
	category_id = models.ForeignKey(Category,null=True,blank=True)
	subcategory_id=models.ForeignKey(SubCategory,null=True,blank=True)
	#category_name=models.CharField(max_length=128,default='cat')
	#subcategory_name=models.CharField(max_length=128,default='subc')
	#status=models.IntegerField(primary_key=True)
	status=models.IntegerField(default=0)
	description=models.TextField()
	objects=JobDetailsManager()



	"""
	def get_category(self):
		
		number=100
		p=JobDetails.objects.all().order_by('-id')[0]
		return u% ('URB',p+1)
		
	urbanId=property(get_category)
	

	def save(self, *args, **kwargs):
		if self.urbanId == "Yoko Ono's blog":
			return True # Yoko shall never have her own blog!
		else:
			super(JobDetails, self).save(*args, **kwargs)
	#  jobcreate_dateTime=models.datetime()
	#  jobWantedDate=models.datetime()
	#  jobWantedtimestart=models.CharField(max_length=128,default='wed 10:10')
	#  jobImage=models.ImageField()
	"""
	def __str__(self):
		return self.subcategory_id.subCat_name




class JobAssign(models.Model):
	id=models.AutoField(primary_key=True)
	jobid=models.ForeignKey(JobDetails,null=True,blank=True)
	vendorid=models.ForeignKey(Vendor,null=True, blank=True)
	datetime=models.CharField(max_length=128,default='20-01-2015')
	payment=models.IntegerField(default=0)
	status=models.IntegerField(default=0)
#	vendorname=models.CharField(max_length=128,default='argss')
	amount=models.IntegerField(default=0)
	feedback=models.CharField(max_length=230,default='Your feedback here..')
#	vname1=models.CharField(max_length=21,default=vendorid.fname)
	#@property
	
#	def update_status(self):
#		self.jobid.status=self.status
#		return self.jobid.status

	def get_vendor_name(self):
		return self.vendorid.fname
	vname=property(get_vendor_name)	

	def get_customer_name(self):
		return self.jobid.customer_id
	customer=property(get_customer_name)

	def get_category(self):
		return self.jobid.category_id
	category=property(get_category)		

	def __str__(self):
		return self.vendorid.fname

#class job_list():
#class job_assignment(): 
#Create your models here.


