from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
	list_filter=('fname','state','city','profile')
	list_display=('id','fname','lname','profile','gender','DOB','state','city','contactNo')


admin.site.register(Vendor,VendorAdmin)
# Register your models here.
