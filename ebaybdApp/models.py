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
    external_video_storage = models.URLField(
        help_text="*Youtube embeded link only", max_length=200, blank=True)
    
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
                              upload_to='images/', help_text='Picture *Automatic convert into 500*500 pixel', blank=True)



class Covid19(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title= models.CharField(
        max_length=100, help_text=' প্শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ', blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    external_video_storage = models.URLField(
        help_text="*Youtube embeded link only", max_length=200, blank=True)
    
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
                              upload_to='images/', help_text='Picture *Automatic convert into 500*500 pixel', blank=True)


