from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/<str:title>/',views.project_view, name='projects'),
    path('covid19/',views.covid19_view, name='Covid19'),
    path('যোগাযোগ/',views.contactus_view, name='contactus'),

]
