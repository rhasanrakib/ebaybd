from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from . models import *
from .forms import *
from django.contrib import messages
from django.core.validators import RegexValidator
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse


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
        page = request.GET.get('page', 1)

        paginator = Paginator(news_list, 4)
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        form = ApplicationForm
        return render(request, 'home.html', {'news': news, 'photos': photos, 'projects': project_list, 'videos': videos, 'quotes': quotes, 'form': form, 'fund': fund})


def project_view(request, pk):
    # project_list = Projects.objects.get(project_title=title)
    # print(project_list)
    project_list = get_object_or_404(Projects, id=pk)
    photos = Image_for_projects.objects.filter(modelForImage=project_list)
    return render(request, 'projects.html', {'context': project_list, 'photos': photos})


def covid19_view(request):
    # project_list = Projects.objects.get(project_title=title)
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
        # committee = VolunteerCommittee.objects.all()
        committee = VolunteerRegistration.objects.filter(accepted=True)
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
        return render(request, 'contactus.html', {'form': form})


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
            messages.warning(request, 'Submission Failed')
            form = VolunteerReg()
            return render(request, 'volunteer_form.html', {'form': form})

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
    return render(request, 'upcoming_events.html', {'context': objects})


def events_details_view(request, pk):

    objects = get_object_or_404(UpcomingEvents, id=pk)
    return render(request, 'events_details.html', {'context': objects})


@login_required
def superuser_dashboard(request):
    getVolList = VolunteerRegistration.objects.filter(accepted=False)
    # Ajax Request
    if request.is_ajax and request.method == "POST":
        context = {}
        # Receive the Ajax from getSelectedData dict key
        getSelectedData = request.POST.getlist(
            'sendSelectedData', request.POST.getlist('sendSelectedData[]'))

        # loads the Json
        for i in getSelectedData:
            data = json.loads(i)

        # Get The Value of these Items
        getKeywords = data['keywords']

        # for volunteer Reg
        if getKeywords == "volunteer":
            action = data['action']
            value = data['value']
            if action == "delete":
                
                VolunteerRegistration.objects.filter(id=int(value)).delete()
            else:
                b = VolunteerRegistration.objects.get(id=int(value))
                b.accepted = True
                b.save()
            # Return the Response to the templates for volunteer
            return JsonResponse({'message': "Updated", 'value': 'tr-'+data['value']}, status=200)

    return render(request, 'login_dashboard_superuser.html', {'volunteer': getVolList})


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # mail = authenticate(request, email=email, password=password)
            # print(username,password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                isValidUser = True
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, 'Failed Submission')
        context = {}
        return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    # return redirect("posts:post_home")
    return redirect("/")
