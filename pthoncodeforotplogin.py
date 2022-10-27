from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Profile
import random

#Create your views here.


def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name= request.POST.get('name')
        mobile= request.POST.get('mobile')

        check_user = User.objects.filter(email = email).first()
        check_profile = profile.objects.filter(mobile = mobile).first()
       
        if check_user  or check_profile:
            context = {'message':'User already exist','class':'danger'}
            return render(request,'register.html',context)
        

        user = User(email = email ,first_name = name)
        user.save()

        otp = str(random.randint(1000 , 9999))

        profile = Profile(user = user, mobile = mobile, otp = otp)
        profile.save()

    return render(request,'register.html')
def otp(request):
    return render(request,'otp.html')
