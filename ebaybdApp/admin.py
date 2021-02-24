from django.contrib import admin
#from . models import Projects,Image_for_projects,Covid19,Image_for_covid19,Donate,ExecutiveCommittee,AdvisorCommittee
#from . models import VolunteerCommittee,About_Us,Photo_Gallery,Image_for_Photo_Gallery

from . models import *

admin.site.register(Donate)
admin.site.register(ExecutiveCommittee)
admin.site.register(AdvisorCommittee)
admin.site.register(VolunteerCommittee)
admin.site.register(About_Us)
admin.site.register(Recent_News)

#Show the images models Inline
class Projects_Images(admin.StackedInline):
    model=Image_for_projects
class Covid19_Images(admin.StackedInline):
    model=Image_for_covid19
class Photo_Gallery_Images(admin.StackedInline):
    model=Image_for_Photo_Gallery
class Video_Gallery_Links(admin.StackedInline):
    model=Link_for_Video_Gallery

#All main models are added to admin

@admin.register(Projects)
class ProjecsAdmin(admin.ModelAdmin):
    inlines=[Projects_Images]

    class Meta:
        model=Projects


@admin.register(Covid19)
class Covid19Admin(admin.ModelAdmin):
    inlines=[Covid19_Images]

    class Meta:
        model=Covid19

@admin.register(Photo_Gallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines=[Photo_Gallery_Images]

    class Meta:
        model=Photo_Gallery

@admin.register(Video_Gallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    inlines=[Video_Gallery_Links]

    class Meta:
        model=Video_Gallery



#All image models are added to admin
'''
@admin.register(Image_for_projects)
class Projects_Images(admin.ModelAdmin):
    pass

@admin.register(Image_for_covid19)
class Covid19_Images(admin.ModelAdmin):
    pass
@admin.register(Image_for_Photo_Gallery)
class CPhoto_Gallery_Images(admin.ModelAdmin):
    pass
'''
