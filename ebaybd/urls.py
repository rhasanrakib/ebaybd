
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('', include('ebaybdApp.urls')),
    path('tinymce/', include('tinymce.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

