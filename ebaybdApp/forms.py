from django import forms

from . models import VolunteerRegistration, BloodDonerRegistration, Application


class VolunteerReg(forms.ModelForm):
    class Meta:
        model = VolunteerRegistration
        fields = '__all__'

        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Input your first name'}),
            'Last_Name': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Input your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control required', 'Placeholder': 'Input your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Ex. 01xxxxxxxxx'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'district': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Ex. Lalmonirhat'}),
            'address': forms.Textarea(attrs={'class': "form-control required"}),
            'about_you': forms.Textarea(attrs={'class': "form-control required"}),
        }


class BloodDonerReg(forms.ModelForm):
    class Meta:
        model = BloodDonerRegistration
        fields = '__all__'

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Input your  name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'Ex. 01xxxxxxxxx'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control required', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': "form-control required"}),
            'bloodGroup': forms.Select(attrs={'class': 'form-control'}),
            'lastDonationDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ['Name', 'email', 'phone', 'subject', 'text']

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'আপনার নাম লিখুন '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'Placeholder': 'আপনার ইমেইল দিন। উদাহরন example@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': '১১ ডিজিটের মোবাইল নম্বর দিন Ex. 01xxxxxxxxx'}),
            'subject': forms.TextInput(attrs={'class': 'form-control required', 'Placeholder': 'কী বিষয়ে জানাতে চান তা লিখুন '}),
            'text': forms.Textarea(attrs={'class': "form-control required", 'Placeholder': 'এখানে লিখুন '}),

        }
