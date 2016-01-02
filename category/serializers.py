from rest_framework import serializers
from category.models import Category,SubCategory



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields=('id','categoryName','keywords','cat_order')


class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=SubCategory
		fields=('id','cat_id','subCat_name','metatags')		