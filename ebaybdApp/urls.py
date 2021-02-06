from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/<str:title>/',views.project_view, name='projects'),
    path('যোগাযোগ/',views.contactus_view, name='contactus'),

]
