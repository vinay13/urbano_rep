# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jobs.models import JobDetails,JobAssign
from jobs.serializers import JobDetailsSerializer,JobAssignSerializer




@api_view(['GET','POST'])
def jobdetails(request):
	if request.method == 'GET':
		jobdetails=JobDetails.objects.all()
		serializer=JobDetailsSerializer(jobdetails,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=JobDetailsSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 






@api_view(['GET','POST'])
def jobassign(request):
	if request.method == 'GET':
		jobassign=JobAssign.objects.all()
		serializer=JobAssignSerializer(jobassign,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=JobAssignSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

















# Create your views here.
