from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone
from tinymce.models import HTMLField
from django.urls import reverse
from django_resized import ResizedImageField

class Projects(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    project_title = models.CharField(max_length=100, help_text=' প্রকল্পের শিরোনাম দিন ')
    description = HTMLField(help_text=' বর্ন্না লিখুন ',blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    slug = AutoSlugField(populate_from='project_title')
    
    slide_image1 = ResizedImageField(size=[500, 500],
        upload_to='images/', help_text='News Picture(*Automatic convert into 500*500 )', blank=True)
    slide_image2 = ResizedImageField(size=[500, 500],
        upload_to='images/', help_text='News Picture(*Automatic convert into 500*500 )', blank=True)
    slide_image3 = ResizedImageField(size=[500, 500],
        upload_to='images/', help_text='News Picture(*Automatic convert into 500*500 )', blank=True)
    slide_image4 = ResizedImageField(size=[500, 500],
        upload_to='images/', help_text='News Picture(*Automatic convert into 500*500 )', blank=True)
    slide_image5 = ResizedImageField(size=[500, 500],
        upload_to='images/', help_text='News Picture(*Automatic convert into 500*500 )', blank=True)
    
    external_video_storage = models.URLField(help_text="*Youtube embeded link only",max_length=200, blank=True)

    #Auto Slug
    def slugify_function(self, content):
        return content.replace('_', '-').lower()
    
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

