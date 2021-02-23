from django.contrib import admin
from . models import Projects,Image_for_projects,Covid19,Image_for_covid19

#admin.site.register(Projects)
#admin.site.register(Image_for_projects)

#Show the images models Inline
class Projects_Images(admin.StackedInline):
    model=Image_for_projects
class Covid19_Images(admin.StackedInline):
    model=Image_for_covid19

#All main models are added to admin

@admin.register(Projects)
class ProjecsAdmin(admin.ModelAdmin):
    inlines=[Projects_Images]

    class Meta:
        model=Projects


@admin.register(Covid19)
class ProjecsAdmin(admin.ModelAdmin):
    inlines=[Covid19_Images]

    class Meta:
        model=Covid19



#All image models are added to admin

@admin.register(Image_for_projects)
class Projects_Images(admin.ModelAdmin):
    pass

@admin.register(Image_for_covid19)
class Covid19_Images(admin.ModelAdmin):
    pass


