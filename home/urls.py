from django.urls import path
from home.views import home

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('Ogrenci_Giris_Sayfasi/debis.php/', home, name='home'),
]