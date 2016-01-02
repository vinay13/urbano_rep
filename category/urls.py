from django.conf.urls import patterns, url

from category import views

urlpatterns = patterns('',
    url(r'^categories/', views.category),
    url(r'^subcategories/',views.subcategory),
    

)
