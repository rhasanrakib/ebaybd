from django.shortcuts import render, get_object_or_404
from . models import Projects, Image_for_projects, Covid19, Image_for_covid19, Donate, AdvisorCommittee, ExecutiveCommittee, VolunteerCommittee


def home_view(request):

    return render(request, 'home.html')


def project_view(request, title):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = get_object_or_404(Projects, project_title=title)
    photos = Image_for_projects.objects.filter(modelForImage=project_list)
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def covid19_view(request):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = Covid19.objects.first()
    photos = Image_for_covid19.objects.all()
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def donate_view(request, title):
    donate_list = Donate.objects.get(project_title=title)
    # print(project_list)
    return render(request, 'projects.html', {'context': donate_list})


def committee_view(request, title):
    committee=""
    page_title=""
    if title == "advisor":
        page_title="উপদেষ্ঠা"
        committee = AdvisorCommittee.objects.all()
    elif title == "executive":
        page_title="কার্যকরী কমিটি"
        committee = ExecutiveCommittee.objects.all()
        
    else:
        page_title="স্বেচ্ছাসেবক"
        committee = VolunteerCommittee.objects.all()
    return render(request,'committee.html',{'context':committee,'title':page_title})

def contactus_view(request):
    return render(request, 'contactus.html')
