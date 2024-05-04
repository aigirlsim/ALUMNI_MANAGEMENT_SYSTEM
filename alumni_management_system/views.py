from django.shortcuts import render,redirect,HttpResponse
from app.EmalBackend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app.models import CustomUser,Alumni
def BASE(request):
    return render(request,'base.html')

def LOGIN(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,
                                         username = request.POST.get('email'),
                                         password=request.POST.get('password'),)
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('staff_home')
            elif user_type == '2':
                return redirect('alumni_home')
            else:
                messages.error(request, "Email and password are invalid!")
                return redirect('login')
        else:
            messages.error(request, "Email and password are invalid!")
            return redirect('login')
        

def dologout(request):
    logout(request)
    return redirect('login')




def PROFILE(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        'user': user,
    }
    print(user)
    return render(request,'profile.html',context)


def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        passowrd =request.POST.get('password')
        # about = request.POST.get('about')
        print(first_name)
    
        try:
          customuser = CustomUser.objects.get(id=request.user.id)

          customuser.first_name = first_name
          customuser.last_name = last_name
        #   customuser.profile_pic =profile_pic
        #   print(profile_pic)
        
          if passowrd !=None and passowrd != "":
              customuser.set_password(passowrd)
          if profile_pic != None and profile_pic != "":
              customuser.profile_pic = profile_pic
          customuser.save()
          messages.success(request,'Your Profile is Updated Successfully!')
          redirect('profile')

        except:
          messages.error(request,'Failed To Update Your Profile!')
        #   print(messages.error)
    return render(request,'profile.html')

def VIEW_ALUMNI(request):
    alumni =Alumni.objects.all()
    
    context = {
        'alumni': alumni,
    }

    return render(request, 'view_alumni.html',context)

