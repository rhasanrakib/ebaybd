from django.shortcuts import render


def home_view(request):
    
    return render(request, 'home.html')


def project_view(request):
    return render(request, 'projects.html')  