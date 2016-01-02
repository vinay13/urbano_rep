from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from category.models import Category,SubCategory
from category.serializers import CategorySerializer,SubCategorySerializer





def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")



@api_view(['GET','POST'])
def category(request):
	if request.method == 'GET':
		category=Category.objects.all()
		serializer=CategorySerializer(category,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=CategorySerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 



@api_view(['GET','POST'])
def subcategory(request):
	if request.method == 'GET':
		category1=SubCategory.objects.all()
		serializer=SubCategorySerializer(category1,many=True)
		return Response(serializer.data)


	elif request.method == 'POST':
	    serializer=SubCategorySerializer(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data,status=status.HTTP_201_CREATED)
	    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

















# Create your views here.
