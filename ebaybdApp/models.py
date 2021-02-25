from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
from tinymce.models import HTMLField
from django.urls import reverse
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError


class Projects(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(
        max_length=100, help_text=' প্রকল্পের শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    slug = AutoSlugField(populate_from='project_title')

    # Auto Slug
    def slugify_function(self, content):
        return content.replace('_', '-')

    def __unicode__(self):
        return self.project_title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("projects", kwargs={'title': self.slug})

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
    slug = AutoSlugField(populate_from='project_title')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title

    # Auto Slug
    def slugify_function(self, content):
        return content.replace('_', '-')

    def __unicode__(self):
        return self.project_title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("donate", kwargs={'title': self.slug})

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
    phone = models.CharField(
        max_length=100, help_text=' ফোন নম্বর ', blank=True)
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
    phone = models.CharField(
        max_length=100, help_text=' ফোন নম্বর ', blank=True)
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
    phone = models.CharField(
        max_length=100, help_text=' ফোন নম্বর ', blank=True)
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
    slug = AutoSlugField(populate_from='project_title')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.project_title

    # Auto Slug
    def slugify_function(self, content):
        return content.replace('_', '-')

    def __unicode__(self):
        return self.project_title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("about", kwargs={'title': self.slug})

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
            raise ValidationError('There is can be only one Covid19 instance')
        return super(Photo_Gallery, self).save(*args, **kwargs)


class Image_for_Photo_Gallery(models.Model):
    modelForImage = models.ForeignKey(Photo_Gallery, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ', blank=True)
    subtitle = models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ', blank=True)
    image = ResizedImageField(size=[500, 500],
                              upload_to='albums/', help_text='Picture *Automatic convert into 500*500 pixel', quality=-1)
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
        max_length=20, help_text='ট্যাগ লিখুন ',default="News")
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    image1 = ResizedImageField(upload_to='news/', help_text='Optional images', quality=-1,blank=True)
    image2 = ResizedImageField(upload_to='news/', help_text='Optional images', quality=-1,blank=True)
    image3 = ResizedImageField(upload_to='news/', help_text='Optional images', quality=-1,blank=True)
    slug = AutoSlugField(populate_from='title')

    # Auto Slug
    def slugify_function(self, content):
        return content.replace('_', '-')

    def __unicode__(self):
        return self.title

    # Metadata
    class Meta:
        ordering = ['-created_date']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse("newsdetails", kwargs={'title': self.slug})

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

class VolunteerRegistration(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    RELIGION_CHOICES=(
        ('I','Islam'),
        ('H','Hindu'),
        ('B','Buddha'),
        ('C','Chirstian'),
    )
    First_Name= models.CharField(max_length=100,blank=False)
    Last_Name= models.CharField(max_length=100,blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=11)
    image = ResizedImageField(size=[300,300],upload_to='volunteers/', help_text='Size will 300*300', quality=-1,blank=True)
    gender= models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True)
    religion= models.CharField(max_length=1, choices=RELIGION_CHOICES,blank=True)
    date_of_birth = models.DateField(blank=True)
    district = models.CharField(max_length=20)
    address = models.TextField()
    about_you= models.TextField(blank=True)
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.First_Name
        