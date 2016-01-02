from django.conf.urls import patterns,url

from jobs import views


urlpatterns=patterns('',
	url(r'^jobdetails/',views.jobdetails),
	url(r'^jobassign/',views.jobassign),

)

