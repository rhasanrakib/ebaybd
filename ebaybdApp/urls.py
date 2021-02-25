from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/<str:title>/',views.project_view, name='projects'),
    path('donate/<str:title>/',views.donate_view, name='donate'),
    path('committee/<str:title>/',views.committee_view, name='committee'),
    path('about/<str:title>/',views.aboutus_view, name='about'),
    path('covid19/',views.covid19_view, name='Covid19'),
    path('photo_gallery/',views.photo_gallery_view, name='photo_gallery'),
    path('videos/',views.video_gallery_view, name='videos'),
    path('যোগাযোগ/',views.contactus_view, name='contactus'),
    path('recent_news/',views.recent_news_view, name='recent_news'),
    path('recent_news/<str:title>/',views.news_view, name='newsdetails'),
    path('our_causes/',views.our_causes_view, name='our_causes'),
    path('volunteer_registration/',views.volunteerRegistration_view, name='volunteerRegistration'),

]
