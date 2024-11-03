"""
URL configuration for PTDACNTT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from benhvienmat import views 
from benhvienmat.views import GetBacSiAPI, HoSoBenhAnAPI, BenhNhanAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    path('viewsAPIBacSi/',GetBacSiAPI.as_view(),name="bac-si-list"),
    path('viewsAPIBenhNhan/',BenhNhanAPI.as_view(),name="benh-nhan-list"),
    path('viewsAPIHoSo/',HoSoBenhAnAPI.as_view(),name="ho-so-list"),
    
    path('viewsAPIBacSi/<int:maBacSi>', GetBacSiAPI.as_view(), name='bac-si-detail'),  # PUT, DELETE
    path('viewsAPIBenhNhan/<int:maBenhNhan>', BenhNhanAPI.as_view(), name='benh-nhan-detail'),  # PUT, DELETE
    path('viewsAPIHoSo/?maBenhAn=<int:maBenhAn>', HoSoBenhAnAPI.as_view(), name='ho-so-detail'),  # PUT, DELETE

    # thu tu thoi gian
    path('danh_sach_hoso_view/', views.danh_sach_hoso_view, name='ho_so_benh_an_theo_thoi_gian'),

    # theo ngay
    path('ho_so_benh_an_date/', views.ho_so_benh_an_theo_ngay, name='ho_so_benh_an_theo_ngay'),


]
