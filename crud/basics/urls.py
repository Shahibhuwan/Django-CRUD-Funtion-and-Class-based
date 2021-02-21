from django.contrib import admin
from django.urls import path
#from .views import CreateStudent, ListStudent, DetailStudent, UpdateStudent, DeleteStudent
from .views import Create, List, Detail, Update, Delete


urlpatterns = [
    #path('create/', CreateStudent.as_view(), name="Add" ),
    #path('/', ListStudent.as_view(), name="List"),
    #path('detail/<pk>/', DetailStudent.as_view(), name="Detail"),
    #path('update/<pk>/', UpdateStudent.as_view(), name="Update"),
    #path('<pk>/delete/', DeleteStudent.as_view(), name="Delete")
    path('create/', Create, name="Add"),
    path('', List, name="List"),
    path('detail/<id>', Detail, name="Detail"),
    path('update/<id>', Update, name="Update"),
    path('delete/<id>', Delete, name="Delete")

    ]

