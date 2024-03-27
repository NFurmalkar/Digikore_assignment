from django.shortcuts import render,redirect
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from testapp.models import Register
from django.http import HttpResponse
import csv
import xlsxwriter


# Create your views here.
@api_view(['POST'])
def OTP(request):

    email = request.data.get('email')
    otp = random.randint(0000,9999)
    print('------------>',otp)
    try:
        sub = "Email OTP"
        mess = f"Your OTP is {otp}"
        to = email
        send_mail(sub,mess,"gavarthor@gmail.com",[to])
    except Exception as e:
        print("Email error--------->",e)
        return Response({'message': "error"})

    params = {"otp": otp, "message": "success"}
    return Response(params)

def register(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        age = request.POST.get('age')
        address = request.POST.get('address')
        academicLevel = request.POST.get('academicLevel')
        university = request.POST.get('university')
        fieldStudy = request.POST.get('fieldStudy')
        studyDestination = request.POST.get('studyDestination')
        enrollment = request.POST.get('enrollment')
        languageProficiency = request.POST.get('languageProficiency')

        Register.objects.create(fullName=fullName,email=email,contact=contact,age=age,address=address,academicLevel=academicLevel,university=university,fieldStudy=fieldStudy,
                                studyDestination=studyDestination,enrollment=enrollment,languageProficiency=languageProficiency)

    return render(request,'register.html')


def showRecords(request):
    data = Register.objects.all()
    params = {'data':data}
    return render(request,'show.html',params)


def getAllCSVData(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=report.csv'

    writer = csv.writer(response)
    header = [field.verbose_name for field in Register._meta.fields]
    writer.writerow(header)
    for obj in Register.objects.all():
        data_row = [getattr(obj,field.name) for field in Register._meta.fields]
        #print(data_row)
        writer.writerow(data_row)
    return response



@api_view(['POST'])
def sms_mobile(request):
    import os
    from twilio.rest import Client
    mobile = request.data.get('mobile')
    print("------>", mobile)

    otp = random.randint(1000, 9999)
    # Set environment variables for your credentials
    account_sid = os.environ['enter Your account_sid']
    auth_token = os.environ['enter your auth_token']
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=f"Sample Test  OTP is {otp}", from_='+91Enter your mobile number', to='+91enter Mobile number')
        print(message)
    except Exception as e:
        print("------>",e)
    return Response({'otp':otp,'message':'message'})

