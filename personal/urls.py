from django.urls import path
from personal.views import personal,BelgeTemplateView,MesajTemplateView,AnketTemplateView,hak,iban,ders,yeni_kayit,ilk_kayit,yabanci,dikey,katki,notgorme,devamsizlik,nott

app_name = 'personal'

urlpatterns = [
    path('debis.php/debis.deu.edu.tr', personal, name='personal'),
    path('OgrenciIsleri/Ogrenci/belge_talep/index.php/debis.deu.edu.tr',BelgeTemplateView.as_view(), name='belgetalebi'),
    path('OgrenciIsleri/Ogrenci/hak_saklama/index.php/debis.deu.edu.tr',hak, name='hak'),
    path('OgrenciIsleri/Ogrenci/iban/index.php/debis.deu.edu.tr',iban, name='iban'),
    path('OgrenciIsleri/Ogrenci/DersProgrami/index.php/debis.deu.edu.tr',ders, name='ders'),
    path('OgrenciIsleri/Ogrenci/IlkKayit/index.php/debis.deu.edu.tr',yeni_kayit, name='yeni_kayit'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelge/index.php/debis.deu.edu.tr',ilk_kayit, name='ilk_kayit'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelgeDeyos/index.php/debis.deu.edu.tr',yabanci, name='yabanci'),
    path('OgrenciIsleri/Ogrenci/OgrenciBelgeDgs/index.php/debis.deu.edu.tr',dikey, name='dikey'),
    path('OgrenciIsleri/Ogrenci/OgrenciHarc/index.php/debis.deu.edu.tr',katki, name='katki'),
    path('DEUWeb/Anket/index.php/debis.deu.edu.tr',AnketTemplateView.as_view(), name='anket'),
    path('OgrenciIsleri/Ogrenci/OgrenciNotu/index.php/debis.deu.edu.tr',notgorme, name='notgorme'),
    path('OgrenciIsleri/Ogrenci/ydy_devamsizlik/index.php/debis.deu.edu.tr',devamsizlik, name='devamsizlik'),
    path('OgrenciIsleri/Ogrenci/transcript/index.php/debis.deu.edu.tr',nott, name='nott'),
    path('DEUWeb/mesaj/index.php/debis.deu.edu.tr',MesajTemplateView.as_view(), name='mesaj'),
]