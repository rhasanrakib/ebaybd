from django.urls import path
from . import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('<str:title>/',views.project_view, name='projects'),

]
