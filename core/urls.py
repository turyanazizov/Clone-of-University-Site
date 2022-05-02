from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# main url https://debis-deu-edu-tr.herokuapp.com/Ogrenci_Giris_Sayfasi/debis.php/debis.deu.edu.tr
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('Ogrenci_Bilgileri/', include('personal.urls', namespace='personal')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
