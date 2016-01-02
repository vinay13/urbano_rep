from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vendor.models import Vendor
from vendor.serializers import VendorSerializer




@api_view(['GET','POST'])
def vendor(request):
	if request.method == 'GET':
		vendor=Vendor.objects.all()
		serializer=VendorSerializer(vendor,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=VendorSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
	    


















# Create your views here.






# Create your views here.
