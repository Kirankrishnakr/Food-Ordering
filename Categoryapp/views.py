from django.shortcuts import render
from django.shortcuts import redirect
from Categoryapp.models import categorydb,Productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.
def categoryfun(req):
    return render(req,"index.html")
def category2fun(req):
    return render(req,"Addcategory.html")
def savecategory(req):
    if req.method =="POST":
        na =req.POST.get('name')
        em =req.POST.get('description')
        im =req.FILES['image']

        obj =categorydb(Name=na,Email=em,Image=im)
        obj.save()
        return redirect(categoryfun)

def displaycategory(req):
    data = categorydb.objects.all()
    return render(req,"Displaycategory.html",{'data':data})

def editcategory(req,dataid):
    data =categorydb.objects.get(id=dataid)
    return render(req,"Editcategory.html",{"data":data})

def updatecategory(req,dataid):
    if req.method =="POST":
        na = req.POST.get('name')
        em = req.POST.get('description')
        try:
            img =req.FILES["image"]
            fs =FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =categorydb.objects.get(id=dataid).Image
        categorydb.objects.filter(id=dataid).update(Name=na,Email=em,Image=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data =categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def productfun(req):
    data =categorydb.objects.all()
    return render(req,"Addproduct.html",{'data':data})

def saveproduct(req):
    if req.method =="POST":
        se =req.POST.get("select")
        pna =req.POST.get("pname")
        pq =req.POST.get("pquan")
        pr =req.POST.get("price")
        de =req.POST.get("description")
        im =req.FILES['image']
        obj =Productdb(categoryname=se,productname=pna,quantity=pq,Price=pr,Des=de,Image=im)
        obj.save()
        return redirect(productfun)
def displayproduct(req):
    data =Productdb.objects.all()
    return render(req,"Displayproduct.html",{'data':data})

def editproduct(req,dataid):
    data=Productdb.objects.get(id=dataid)
    da =categorydb.objects.all()
    return render(req,"Editproduct.html",{'data':data,'da':da})

def updateproduct(req,dataid):
    if req.method =="POST":
        se = req.POST.get("select")
        pna = req.POST.get("pname")
        pq = req.POST.get("pquan")
        pr = req.POST.get("price")
        de = req.POST.get("description")
        try:
            img =req.FILES['image']
            fs =FileSystemStorage()
            file= fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = Productdb.objects.get(id=dataid).Image
            Productdb.objects.filter(id=dataid).update(categoryname=se,productname=pna,quantity=pq,Price=pr,Des=de,Image=file)
            return redirect(displayproduct)

def deleteproduct(req,dataid):
    data =Productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def index2fun(req):
    return render(req,"index2.html")

def Adminpage(request):
    if request.method =="POST":
        username_r =request.POST.get('username')
        password_r =request.POST.get('password')
        if User.objects.filter(username__contains =username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']= username_r
                request.session['password']= password_r
                return redirect(categoryfun)
            else:
                return redirect(index2fun)
        else:
            return redirect(index2fun)




def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index2fun)

















