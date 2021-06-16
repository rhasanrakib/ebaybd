from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
from tinymce.models import HTMLField
from django.urls import reverse
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Projects(models.Model):

    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(
        max_length=100, help_text=' প্রকল্পের শিরোনাম দিন ')
    bannerImage = ResizedImageField(
        upload_to='images/', help_text='এই ছবিটি আপলোড করলে তা হোমপেইজের শেষের অংশের স্লাইডে যুক্ত হবে। সেটি না করতে চাইলে ফাকা রাখুন ', blank=True, quality=-1)
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __unicode__(self):
        return self.project_title

    # Metadata

    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("projects", kwargs={'pk': str(self.id)})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title


class Image_for_projects(models.Model):
    modelForImage = models.ForeignKey(Projects, on_delete=models.CASCADE)

    image = ResizedImageField(size=[500, 500],
                              upload_to='images/', help_text='Picture *Automatic convert into 500*500 pixel', blank=True, quality=-1)


class Covid19(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and Covid19.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Covid19 instance')
        return super(Covid19, self).save(*args, **kwargs)


class Image_for_covid19(models.Model):
    modelForImage = models.ForeignKey(Covid19, on_delete=models.CASCADE)

    image = ResizedImageField(size=[500, 500],
                              upload_to='images/', help_text='Picture *Automatic convert into 500*500 pixel', blank=True, quality=-1)


class Donate(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(
        max_length=100, help_text=' প্রকল্পের শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    #slug = AutoSlugField(populate_from='project_title')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title

    def __unicode__(self):
        return self.project_title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("donate", kwargs={'pk': str(self.id)})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title


class ExecutiveCommittee(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    serial = models.IntegerField(unique=True, blank=False)
    name = models.CharField(
        max_length=100, help_text=' নাম  ')
    designation = models.CharField(
        max_length=100, help_text=' পদবী ')
    occupation = models.CharField(
        max_length=100, help_text=' পেশা ', blank=True)
    organization = models.CharField(
        max_length=100, help_text=' প্রতিষ্ঠান ', blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=14,
                             help_text=' ফোন নম্বর ', blank=True)  # validators should be a list
    Address = models.CharField(
        max_length=100, help_text=' ঠিকানা ', blank=True)
    image = ResizedImageField(
        upload_to='images/', help_text='Profile Picture', blank=True, quality=-1)

    def __str__(self):
        s = str(self.serial)+" "+self.name
        return s

    # Metadata
    class Meta:
        ordering = ['serial']


class AdvisorCommittee(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    serial = models.IntegerField(unique=True, blank=False)
    name = models.CharField(
        max_length=100, help_text=' নাম  ')
    designation = models.CharField(
        max_length=100, help_text=' পদবী ')
    occupation = models.CharField(
        max_length=100, help_text=' পেশা ', blank=True)
    organization = models.CharField(
        max_length=100, help_text=' প্রতিষ্ঠান ', blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=14,
                             help_text=' ফোন নম্বর ', blank=True)  # validators should be a list
    Address = models.CharField(
        max_length=100, help_text=' ঠিকানা ', blank=True)
    image = ResizedImageField(
        upload_to='images/', help_text='Profile Picture', blank=True, quality=-1)

    def __str__(self):
        s = str(self.serial)+" "+self.name
        return s

    # Metadata
    class Meta:
        ordering = ['serial']


class VolunteerCommittee(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    serial = models.IntegerField(unique=True, blank=False)
    name = models.CharField(
        max_length=100, help_text=' নাম  ')
    designation = models.CharField(
        max_length=100, help_text=' পদবী ', default='স্বেচ্ছাসেবক')
    occupation = models.CharField(
        max_length=100, help_text=' পেশা ', blank=True)
    organization = models.CharField(
        max_length=100, help_text=' প্রতিষ্ঠান ', blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    phone = models.CharField(validators=[phone_regex], max_length=14,
                             help_text=' ফোন নম্বর ', blank=True)  # validators should be a list

    Address = models.CharField(
        max_length=100, help_text=' ঠিকানা ', blank=True)
    image = models.ImageField(
        upload_to='images/', help_text='Profile Picture', blank=True)

    def __str__(self):
        s = str(self.serial)+" "+self.name
        return s

    # Metadata
    class Meta:
        ordering = ['serial']


class About_Us(models.Model):

    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(
        max_length=100, help_text='  শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title

    def __unicode__(self):
        return self.project_title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        return reverse("about", kwargs={'pk': str(self.id)})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title


class Photo_Gallery(models.Model):
    """A typical class defining a model, derived from the Model class."""

    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Photos"

    def save(self, *args, **kwargs):
        if not self.pk and Photo_Gallery.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one instance')
        return super(Photo_Gallery, self).save(*args, **kwargs)


class Image_for_Photo_Gallery(models.Model):
    modelForImage = models.ForeignKey(Photo_Gallery, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ', blank=True)
    subtitle = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ', blank=True)
    image = ResizedImageField(
        upload_to='albums/', help_text='Picture', quality=-1)
    show_in_homepage = models.BooleanField()

    def __unicode__(self):
        return self.title


class Video_Gallery(models.Model):
    """A typical class defining a model, derived from the Model class."""

    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "Videos"

    def save(self, *args, **kwargs):
        if not self.pk and Video_Gallery.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Covid19 instance')
        return super(Video_Gallery, self).save(*args, **kwargs)


class Link_for_Video_Gallery(models.Model):
    modelForImage = models.ForeignKey(Video_Gallery, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ', blank=True)
    external_video_storage = models.URLField(
        help_text="*Youtube embeded link only ex.https://www.youtube.com/embed/ebRd6BBlibc", max_length=200)
    show_on_homepage = models.BooleanField()

    def __unicode__(self):
        return self.title


class Recent_News(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    title = models.CharField(
        max_length=100, help_text=' শিরোনাম দিন ')
    created_date = models.DateTimeField('date created', default=timezone.now)
    reporter_name = models.CharField(
        max_length=100, help_text='রিপর্টারের নাম ')
    tag = models.CharField(
        max_length=20, help_text='ট্যাগ লিখুন ', default="News")
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    image1 = ResizedImageField(
        upload_to='news/', help_text='Optional images', quality=-1, blank=True)
    image2 = ResizedImageField(
        upload_to='news/', help_text='Optional images', quality=-1, blank=True)
    image3 = ResizedImageField(
        upload_to='news/', help_text='Optional images', quality=-1, blank=True)

    def __unicode__(self):
        return self.title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("newsdetails", kwargs={'pk': str(self.id)})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title


class VolunteerRegistration(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    RELIGION_CHOICES = (
        ('I', 'Islam'),
        ('H', 'Hindu'),
        ('B', 'Buddha'),
        ('C', 'Chirstian'),
    )
    name = models.CharField(max_length=100, blank=False)

    email = models.EmailField(blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    # validators should be a list
    phone = models.CharField(validators=[phone_regex], max_length=14)
    designation = models.CharField(
        max_length=100, help_text=' পদবী ', default='স্বেচ্ছাসেবক')
    occupation = models.CharField(
        max_length=100,  blank=True)
    organization = models.CharField(
        max_length=100, blank=True)
    image = ResizedImageField(size=[300, 300], upload_to='volunteers/',
                              help_text='Size will be 300*300', quality=-1, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    address = models.TextField()
    about_you = models.TextField(blank=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.First_Name


class Quotes(models.Model):
    serial = models.IntegerField(unique=True, blank=False)
    name = models.CharField(
        max_length=100, help_text=' নাম  ')
    designation = models.CharField(
        max_length=100, help_text=' পদবী ')
    occupation = models.CharField(
        max_length=100, help_text=' পেশা ', blank=True)
    organization = models.CharField(
        max_length=100, help_text=' প্রতিষ্ঠান ', blank=True)
    image = ResizedImageField(
        upload_to='Quotes/', help_text='Profile Picture', blank=True, quality=-1)
    description = HTMLField(help_text=' বানী লিখুন ', blank=True)

    def __str__(self):
        s = str(self.serial)+" "+self.name
        return s

    class Meta:
        ordering = ['serial']


class BloodDonerRegistration(models.Model):

    GROUP_CHOICES = (
        ('A+', 'A+(VE)'),
        ('A-', 'A-(NE)'),
        ('B+', 'B+(VE)'),
        ('B-', 'B-(NE)'),
        ('O+', 'O+(VE)'),
        ('O-', 'O-(NE)'),
    )
    Name = models.CharField(max_length=100, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    # validators should be a list
    phone = models.CharField(validators=[phone_regex], max_length=14)
    bloodGroup = models.CharField(
        max_length=2, choices=GROUP_CHOICES)
    date_of_birth = models.DateField(help_text='Must be 18 years')
    address = models.TextField()
    lastDonationDate = models.DateField(blank=True, null=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.Name


class Application(models.Model):
    created_date = models.DateTimeField('date created', default=timezone.now)
    Name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    # validators should be a list
    phone = models.CharField(validators=[phone_regex], max_length=14)

    subject = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        strs = str(self.created_date)+" "+self.Name
        return strs


class DonationInformation(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    donar_address = models.TextField(blank=True)
    phone = models.CharField(
        validators=[phone_regex], max_length=14, blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        strs = self.account_number+" "+self.name
        return strs


class UpcomingEvents(models.Model):
    event_date = models.DateTimeField(
        help_text="YYYY/MM/DD HH:MM:SS(International format)")
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    description = HTMLField(help_text=' Description ', blank=True)

    def get_absolute_url(self):
        return reverse('events_details', kwargs={'pk': self.pk})

    def __str__(self):
        strs = str(self.event_date)+" "+self.title
        return strs

    class Meta:
        ordering = ['-event_date']


class FundRaise(models.Model):
    created_date = models.DateTimeField('date created', default=timezone.now)
    title = models.CharField(max_length=200)
    quote = models.CharField(max_length=200, blank=True)
    description = HTMLField(help_text=' Description ', blank=True)
    targeted_amount = models.IntegerField(default=0)
    raised_amount = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images")
    active = models.BooleanField()
    url_field = models.ForeignKey(Donate, on_delete=models.SET_NULL, blank=True,
                                  null=True)

    @property
    def percentage(self):
        return int((self.raised_amount/self.targeted_amount) * 100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


class Misc(models.Model):
    """Model definition for Misc."""

    created_date = models.DateTimeField('date created', default=timezone.now)
    about_us = HTMLField(help_text=' আমাদের সম্পর্কে ', blank=True)
    our_works = HTMLField(help_text=' আমাদের কার্যক্রম সমূহ ', blank=True)
    volunteer_context = HTMLField(
        help_text=' স্বেচ্ছাসেবক প্রোগ্রামের জন্য নিবন্ধন', blank=True)
    image = ResizedImageField(
        upload_to='Quotes/', help_text='volunteer context pic', blank=True, quality=-1)
    footer_about_us = HTMLField(help_text='আমাদের কার্যক্রম', blank=True)
    address = HTMLField(help_text='যোগাযোগ করুন', blank=True)
    google_map_link = models.URLField(blank=True)
    email1 = models.EmailField(blank=True)
    email2 = models.EmailField(blank=True)
    email3 = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the format: '+8801xxxxxxxxx'.")

    phone1 = models.CharField(
        validators=[phone_regex], max_length=14, blank=True)
    phone2 = models.CharField(
        validators=[phone_regex], max_length=14, blank=True)

    class Meta:
        """Meta definition for Misc."""

        verbose_name = 'Misc'
        verbose_name_plural = 'Miscs'

    def __str__(self):
        return "Misc"
