from django.urls.conf import path
from .models import Task
from .views import apiOverView, tasklist, taskdetail, taskcreate, taskupdate, taskdelete

urlpatterns = [
    path('',apiOverView, name="API"),
    path('list/', tasklist, name="list"),
    path('detail/<id>', taskdetail, name="detail"),
     path('create', taskcreate, name="create"),
      path('update/<id>', taskupdate, name="update"),
      path('delete/<id>', taskdelete, name="delete")

]

