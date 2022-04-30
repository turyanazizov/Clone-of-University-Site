from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('personal/', include('personal.urls', namespace='personal')),
] 
if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
