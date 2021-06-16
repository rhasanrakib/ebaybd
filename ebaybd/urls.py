
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls

urlpatterns = [
    path('admin_panel/', admin.site.urls),
    path('', include('ebaybdApp.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

