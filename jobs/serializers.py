from rest_framework import serializers
from jobs.models import JobDetails,JobAssign

class JobDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model=JobDetails
		fields='__all__'


class JobAssignSerializer(serializers.ModelSerializer):
	class Meta: 
		model=JobAssign
		fields='__all__'



