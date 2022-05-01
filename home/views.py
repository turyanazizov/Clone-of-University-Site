from django.shortcuts import redirect, render

def home(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        emailHost=request.POST.get("emailHost")
        key1='turgut.karakelle'
        key2='786502Si'
        key3='ogr.deu.edu.tr'
        if username==key1 and password==key2 and emailHost==key3:
            return redirect('personal:personal')
    return render(request,'index.html')
