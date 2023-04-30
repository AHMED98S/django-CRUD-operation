from django.contrib import admin
from django.urls import path
from enroll.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add_show, name="addshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('update/<int:id>/', views.update_data, name="updatedata"),
]