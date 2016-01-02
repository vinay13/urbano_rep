from django.conf.urls import patterns, url

from customer import views

urlpatterns = patterns('',
    url(r'^customers/', views.customer),
    
    

)

