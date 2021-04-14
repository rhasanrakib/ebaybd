from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from . models import *
from .forms import *
from django.contrib import messages
from django.core.validators import RegexValidator
from datetime import datetime

def home_view(request):

    news_list = Recent_News.objects.all()
    project_list = Projects.objects.exclude(bannerImage="")
    videos = Link_for_Video_Gallery.objects.filter(show_on_homepage=True)
    photos = Image_for_Photo_Gallery.objects.filter(show_in_homepage=True)
    quotes = Quotes.objects.all()
    fund = FundRaise.objects.filter(active=True)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly Submitted')
            form = ApplicationForm()
            return redirect("home")
        else:
            messages.warning(request, 'Fail to Submit')
            return redirect("home")

    else:

        form = ApplicationForm
        return render(request, 'home.html', {'news': news_list, 'photos': photos, 'projects': project_list, 'videos': videos, 'quotes': quotes, 'form': form,'fund':fund})


def project_view(request, pk):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = get_object_or_404(Projects, id=pk)
    photos = Image_for_projects.objects.filter(modelForImage=project_list)
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def covid19_view(request):
    #project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = Covid19.objects.first()
    photos = Image_for_covid19.objects.all()
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def donate_view(request, pk):
    
    donate_list = Donate.objects.get(id=pk)
    # print(project_list)
    return render(request, 'projects.html', {'context': donate_list})

def donarForm_view(request):
    if request.method == 'POST':
        form = DonationInfoForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly Submitted')
            form = DonationInfoForm()
            return redirect("doner_info_submit")
        else:
            messages.warning(request, 'Fail to Submit')
            return redirect("doner_info_submit")

    else:
        form = DonationInfoForm
        return render(request, 'donarform.html', {'form': form})


def aboutus_view(request, pk):
    aboutus_list = About_Us.objects.get(id=pk)
    # print(project_list)
    return render(request, 'projects.html', {'context': aboutus_list})


def committee_view(request, title):
    committee = ""
    page_title = ""
    if title == "advisor":
        page_title = "উপদেষ্ঠা"
        committee = AdvisorCommittee.objects.all()
    elif title == "executive":
        page_title = "কার্যকরী কমিটি"
        committee = ExecutiveCommittee.objects.all()

    else:
        page_title = "স্বেচ্ছাসেবক"
        committee = VolunteerCommittee.objects.all()
    return render(request, 'committee.html', {'context': committee, 'title': page_title})


def contactus_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfuly Submitted')
            form = ApplicationForm()
            return redirect("contactus")
        else:
            messages.warning(request, 'Fail to Submit')
            return redirect("contactus")
    else:
        form = ApplicationForm()
        return render(request, 'contactus.html',{'form':form})


def photo_gallery_view(request):
    photos = Image_for_Photo_Gallery.objects.all()
    project_title = {
        'project_title': "ফটো গ্যালারী",
    }
    return render(request, 'projects.html', {'context': project_title, 'photos': photos})


def video_gallery_view(request):
    videos = Link_for_Video_Gallery.objects.all()
    project_title = {
        'project_title': "ভিডিও গ্যালারী",
    }
    return render(request, 'projects.html', {'context': project_title, 'videos': videos})


def recent_news_view(request):
    news_list = Recent_News.objects.all()
    return render(request, 'pressbriefing.html', {'news': news_list})


def news_view(request, pk):
    news_list = Recent_News.objects.all().exclude(id=pk)
    news = get_object_or_404(Recent_News, id=pk)
    return render(request, 'news.html', {'news': news, 'sug': news_list})


def our_causes_view(request):
    projects = Projects.objects.all()
    return render(request, 'our-causes.html', {'projects': projects})


def volunteerRegistration_view(request):
    if request.method == 'POST':
        form = VolunteerReg(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            form = VolunteerReg()
            return redirect("home")

    else:
        form = VolunteerReg()
        return render(request, 'volunteer_form.html', {'form': form})


def donate_blood_view(request):
    donar = BloodDonerRegistration.objects.all()
    return render(request, 'donate_blood.html', {'context': donar})


def doner_reg_view(request):

    if request.method == 'POST':
        form = BloodDonerReg(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            form = BloodDonerReg()
            donar = BloodDonerRegistration.objects.all()
            return redirect('donate_blood')

    else:
        form = BloodDonerReg()
        return render(request, 'doner_form.html', {'form': form})

def upcoming_events_view(request):
    today = datetime.today()
    objects = UpcomingEvents.objects.filter(event_date__gte=today)
    return render(request,'upcoming_events.html',{'context':objects})

def events_details_view(request, pk):
    objects =get_object_or_404(UpcomingEvents, id=pk)
    return render(request,'events_details.html',{'context':objects})
