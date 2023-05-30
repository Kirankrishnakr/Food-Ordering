from django.urls import path
from Categoryapp import views

urlpatterns =[
    path('categoryfun/',views.categoryfun,name="categoryfun"),
    path('category2fun/',views.category2fun,name="category2fun"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('productfun/',views.productfun,name="productfun"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
    path('index2fun/',views.index2fun,name="index2fun"),
    path('Adminpage/',views.Adminpage,name="Adminpage"),
    path('Admin_Logout/',views.Admin_Logout,name="Admin_Logout"),
]

