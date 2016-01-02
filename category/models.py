from django.db import models


class Category(models.Model):
	id=models.AutoField(primary_key=True)
	cat_order=models.CharField(max_length=128,default='cat_order') 

	categoryName=models.CharField(max_length=128,default='category')
	keywords=models.CharField(max_length=128,default='keywords')
	
    
    #dateTime=models.dateTime()


	def __str__(self):
		return self.categoryName




class SubCategory(models.Model):
	id=models.AutoField(primary_key=True)
	cat_id=models.ForeignKey(Category)
#	dateTime=models.dateTime()
	subCat_name=models.CharField(max_length=128,default='tv repair')
	metatags=models.CharField(max_length=128,default='tcc')


	def __str__(self):
		return self.subCat_name




# Create your models here.
