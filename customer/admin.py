from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
	list_filter=('fname','state','city')
	list_display=('id','fname','lname','DOB','state','city','contactno')


admin.site.register(Customer,CustomerAdmin)


# Register your models here.


# Register your models here.
