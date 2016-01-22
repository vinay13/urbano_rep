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




@api_view(['GET', 'PUT', 'DELETE'])
def jobdetails_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        jobdetails2 = JobDetails.objects.get(pk=pk)
    except JobDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobDetailsSerializer(jobdetails2)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobDetailsSerializer(jobdetails2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        jobdetails2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#job detail status
@api_view(['GET'])
def jobdetails_status(request,status):
	if request.method == 'GET':
		jobdetails3=JobDetails.objects.filter(status=status)
		serializer=JobDetailsSerializer(jobdetails3,many=True)
		return Response(serializer.data)





# job asssign serializers

#job assign get n post
@api_view(['GET','POST'])
def jobassign(request):
	if request.method == 'GET':
		jobassign=JobAssign.objects.all()
		serializer=JobAssignSerializer(jobassign,many=True)
		return Response(serializer.data)

		""" 
		def jobfilter(self):
			status = self.request.status
			return JobAssign.objects.filter(status=status)
		"""			


	elif request.method == 'POST':
	    serializer=JobAssignSerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


#job assign detail serialization
@api_view(['GET', 'PUT', 'DELETE'])
def jobassign_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        jobassign2 = JobAssign.objects.get(pk=pk)
    except JobAssign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobAssignSerializer(jobassign2)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobAssignSerializer(jobassign2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        jobassign2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
@api_view(['GET'])
def jobassign_detail_status(request, status ):
    
    try:
        jobassign3 = JobAssign.objects.get(status=status)
    except JobAssign.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobAssignSerializer(jobassign3)
        return Response(serializer.data)
"""
 

#job assign status serialization
@api_view(['GET'])
def jobassign_status(request,status):
	if request.method == 'GET':
		jobassign=JobAssign.objects.filter(status=status)
		serializer=JobAssignSerializer(jobassign,many=True)
		return Response(serializer.data)

@api_view(['GET'])
def jobassign_payment(request,payment):
	if request.method == 'GET':
		jobassign=JobAssign.objects.filter(payment=payment)
		serializer=JobAssignSerializer(jobassign,many=True)
		return Response(serializer.data)






# Create your views here.
