from django.conf.urls import patterns,url

from vendor import views

urlpatterns=patterns('',
	url(r'^vendors/',views.vendor),

)





