from django.shortcuts import render
from Categoryapp.models import categorydb,Productdb

# Create your views here.
def webfun(req):
    data =categorydb.objects.all()
    return render(req,"webb.html",{'data':data})

def contact(req):
    return render(req,"contact.html")

def brandfun(req,catg):
    products = Productdb.objects.filter(categoryname=catg)
    return render(req,"brand.html" ,{'products':products})

def morefun(request,dataid):
    data = Productdb.objects.get(id=dataid)
    return render(request,"more.html",{'data':data})