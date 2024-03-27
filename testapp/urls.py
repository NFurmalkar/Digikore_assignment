from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register,name="register"),
    path('otp/', views.OTP,name="getOTP"),
    path('showRecords/', views.showRecords,name="showRecords"),
    path('getAllCSVData/', views.getAllCSVData,name="getCSVData"),
    path('sendSms/', views.sms_mobile,name="sms"),
]
