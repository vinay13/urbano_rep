from django.contrib import admin
from .models import JobDetails,JobAssign

class JobDetailsAdmin(admin.ModelAdmin):
	list_filter=('category_name','WantedDate','subcategory_name')
	list_display=('id','customer_name','WantedDate','Wantedtimestart','category_name','subcategory_name','status','description','createdateTime')



class JobAssignAdmin(admin.ModelAdmin):
	list_filter=('payment','status')
	list_display=('id','jobid','vendorid','vendorname','datetime','payment','status')


admin.site.register(JobDetails,JobDetailsAdmin)
admin.site.register(JobAssign,JobAssignAdmin)



# Register your models here.
