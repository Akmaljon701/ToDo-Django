from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginview),
    path('logout/', logoutview),
    path('home/', asosiy),
    path('delete/<int:son>/', delete),
    path('edit/<int:son>/', edit),
]
