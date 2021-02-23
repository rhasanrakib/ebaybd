from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/<str:title>/',views.project_view, name='projects'),
    path('donate/<str:title>/',views.donate_view, name='donate'),
    path('committee/<str:title>/',views.committee_view, name='committee'),
    path('covid19/',views.covid19_view, name='Covid19'),
    path('যোগাযোগ/',views.contactus_view, name='contactus'),

]
