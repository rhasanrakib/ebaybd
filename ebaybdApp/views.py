from django.shortcuts import render
from . models import Projects

def home_view(request):
    
    return render(request, 'home.html')


def project_view(request,title):
    project_list = Projects.objects.get(project_title=title)
    print(project_list)
    return render(request, 'projects.html',{'context':project_list})  

def contactus_view(request):
    return render(request, 'contactus.html')