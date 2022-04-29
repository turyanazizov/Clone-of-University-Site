from django.urls import path
from personal.views import personal,belgetalebi,hak,iban,ders,yeni_kayit,ilk_kayit,yabanci,dikey,katki,anket,mesaj,notgorme,devamsizlik,nott

app_name = 'personal'

urlpatterns = [
    path('personal/', personal, name='personal'),
    path('a/',belgetalebi, name='belgetalebi'),
    path('b/',hak, name='hak'),
    path('c/',iban, name='iban'),
    path('d/',ders, name='ders'),
    path('f/',yeni_kayit, name='yeni_kayit'),
    path('r/',ilk_kayit, name='ilk_kayit'),
    path('y/',yabanci, name='yabanci'),
    path('u/',dikey, name='dikey'),
    path('g/',katki, name='katki'),
    path('o/',anket, name='anket'),
    path('ui/',notgorme, name='notgorme'),
    path('ik/',devamsizlik, name='devamsizlik'),
    path('km/',nott, name='nott'),
    path('ijn/',mesaj, name='mesaj'),
]