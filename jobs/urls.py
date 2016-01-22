from django.conf.urls import patterns,url

from jobs import views


urlpatterns=patterns('',
	url(r'^jobdetails/$',views.jobdetails),
	url(r'^jobdetails/(?P<pk>[0-9]+)/$',views.jobdetails_detail),
	url(r'^jobdetails/status/(?P<status>[a-z]+)/$',views.jobdetails_status),
	
	url(r'^jobassign/$',views.jobassign),
	url(r'^jobassign/(?P<pk>[0-9]+)/$',views.jobassign_detail),
	url(r'^jobassign/status/(?P<status>[a-z]+)/$',views.jobassign_status),
	url(r'^jobassign/payment/(?P<payment>[a-z]+)/$',views.jobassign_payment),
	
)

