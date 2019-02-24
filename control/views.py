from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import internship
from .models import NewUserModel
from .models import commission
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import * # formlar
from django.contrib.auth import * #Login - Logout
from django.contrib.auth.decorators import * #görünüm gizlenme
from django.http import * # Http komutları



def giris(request):
    #Giriş yapan bidaha giremesin
    oku = request.user.id
    if(oku):
        if len(str(request.user))>4:
            return HttpResponseRedirect('/ogrenci/')
        else:
            return HttpResponseRedirect('/akdmsyn/')
    
    form = AuthenticationForm
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        giris_kontrol = AuthenticationForm(data=request.POST)
        if(giris_kontrol.is_valid()):
            kullanici = authenticate(username=username,password=password)
            login(request,kullanici)
        if len(str(request.user))>4:
            return HttpResponseRedirect('/ogrenci/')
        else:
            return HttpResponseRedirect('/akdmsyn/')
    
    return render(request,'giris.html',locals())
 
def ogrenci(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    return render(request,'ogrenci.html',locals())

def akdmsyn(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    return render(request,'akdmsyn.html',locals())
 
def cikis_yap(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    logout(request)
    return HttpResponseRedirect('/')

def staj(request):
    if request.method=='POST':
        return HttpResponseRedirect('/')
    else:
        internships = internship.objects.all()
        return render(request,'staj.html',{"internships":internships})


def stajekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('/')
    else:
        
        sehir=request.GET.get("sehir")
        company=request.GET.get("company")
        baslangic=request.GET.get("baslangic")
        bitis=request.GET.get("bitis")
        gun=request.GET.get("gun")
        dosya=request.GET.get("dosya")
        newinternship=internship(student=request.user,studentid=request.user,city=sehir,company=company,strtdate=baslangic,fnshdate=bitis,day=gun,files=dosya)   
        newinternship.save()
        internships = internship.objects.all()
        return render(request,'staj.html',{"internships":internships})



def delete (request,id):
    DLT=get_object_or_404(internship,id=id)
    DLT.delete()
    return redirect("/staj",{'id':id})

def bilgi(request):
    if request.method=='POST':
        return HttpResponseRedirect('/')
    else:
        return render(request,'bilgiler.html')



def bilgidegis(request):
    if request.method=="GET":
        return HttpResponseRedirect('/')
    else:
        user=get_object_or_404(NewUserModel,id=request.user.id)
        
        user.phone=request.POST.get('tel')
        user.password=request.POST.get('sifre')
        user.save()
        return  redirect("/bilgi")

def rapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/akdmsyn')
    else:
        internships = internship.objects.all()
        return render(request,'rapor.html',{"internships":internships})
