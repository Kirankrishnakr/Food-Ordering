from django.urls import path
from webappp import views

urlpatterns =[
    path('webfun/',views.webfun,name="webfun"),
    path('contact/',views.contact,name="contact"),
    path('brandfun/<catg>/',views.brandfun,name="brandfun"),
    path('morefun/<int:dataid>/',views.morefun,name="morefun"),
]