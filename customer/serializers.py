from rest_framework import serializers
from customer.models import Customer





class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields=('id','fname','lname','DOB','contactno','city','state','landmark','address','pincode')










