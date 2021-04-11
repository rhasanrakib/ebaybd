from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('project/<int:pk>/',views.project_view, name='projects'),
    path('donate/<int:pk>/',views.donate_view, name='donate'),
    path('committee/<str:title>/',views.committee_view, name='committee'),
    path('about/<int:pk>/',views.aboutus_view, name='about'),
    path('covid19/',views.covid19_view, name='Covid19'),
    path('photo_gallery/',views.photo_gallery_view, name='photo_gallery'),
    path('videos/',views.video_gallery_view, name='videos'),
    path('contact-us/',views.contactus_view, name='contactus'),
    path('recent_news/',views.recent_news_view, name='recent_news'),
    path('recent_news/<int:pk>/',views.news_view, name='newsdetails'),
    path('our_causes/',views.our_causes_view, name='our_causes'),
    path('volunteer_registration/',views.volunteerRegistration_view, name='volunteerRegistration'),
    path('donate_blood_list/',views.donate_blood_view, name='donate_blood'),
    path('donate_blood_register/',views.doner_reg_view, name='doner_reg'),
    path('donar-info-submit-form/',views.donarForm_view, name='doner_info_submit')
]
