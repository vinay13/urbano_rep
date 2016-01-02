from rest_framework import serializers
from jobs.models import JobDetails,JobAssign

class JobDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model=JobDetails
		fields=('id','customer_name','createdateTime','Wantedtimestart','category_name','subcategory_name','status','description')





class JobAssignSerializer(serializers.ModelSerializer):
	class Meta: 
		model=JobAssign
		fields=('id','jobid','vendorid','vendorname','datetime','payment','status')
