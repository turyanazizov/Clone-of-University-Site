from django.urls import path
from personal.views import personal,belgetalebi,hak,iban,ders,yeni_kayit,ilk_kayit,yabanci,dikey,katki,anket,mesaj,notgorme,devamsizlik,nott

app_name = 'personal'

urlpatterns = [
    path('', personal, name='personal'),
    path('OgrenciIsleri/Ogrenci/belge_talep/index.php',belgetalebi, name='belgetalebi'),
    path('OgrenciIsleri/Ogrenci/hak_saklama/index.php',hak, name='hak'),
    path('OgrenciIsleri/Ogrenci/iban/index.php',iban, name='iban'),
    path('OgrenciIsleri/Ogrenci/DersProgrami/index.php',ders, name='ders'),
    path('OgrenciIsleri/Ogrenci/IlkKayit/index.php',yeni_kayit, name='yeni_kayit'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelge/index.php',ilk_kayit, name='ilk_kayit'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelgeDeyos/index.php',yabanci, name='yabanci'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelgeDgs/index.php',dikey, name='dikey'),
    path('OgrenciIsleri/Ogrenci/OgrenciHarc/index.php',katki, name='katki'),
    path('DEUWeb/Anket/index.php',anket, name='anket'),
    path('OgrenciIsleri/Ogrenci/OgrenciNotu/index.php',notgorme, name='notgorme'),
    path('OgrenciIsleri/Ogrenci/ydy_devamsizlik/index.php',devamsizlik, name='devamsizlik'),
    path('OgrenciIsleri/Ogrenci/transcript/index.php',nott, name='nott'),
    path('DEUWeb/mesaj/index.php',mesaj, name='mesaj'),
    
]