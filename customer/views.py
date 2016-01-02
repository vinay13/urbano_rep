from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Customer
from customer.serializers import CustomerSerializer




@api_view(['GET','POST'])
def customer(request):
	if request.method == 'GET':
		category=Customer.objects.all()
		serializer=CustomerSerializer(category,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=CustomerSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 













# Create your views here.
