from django.contrib import admin
from .models import Category,SubCategory



class CategoryAdmin(admin.ModelAdmin):
	list_filter=('id','categoryName','cat_order')
	list_display=('id','categoryName','cat_order','keywords')


class SubCategoryAdmin(admin.ModelAdmin):
	list_filter=('id','subCat_name')
	list_display=('id','subCat_name','cat_id','metatags')




admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)



# Register your models here.
