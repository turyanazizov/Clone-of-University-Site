from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debis.php/', include('home.urls', namespace='home')),
    path('debis.php/', include('personal.urls', namespace='personal')),
]
