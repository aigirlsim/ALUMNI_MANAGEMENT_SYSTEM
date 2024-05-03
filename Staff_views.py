from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year, Alumni, Event,PJob
from app.models import CustomUser
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    alumni_count  = Alumni.objects.all().count()
    event_count = Event.objects.all().count()
    job_count = PJob.objects.all().count()

    student_gender_male = Alumni.objects.filter(gender='Male').count()
    student_gender_female = Alumni.objects.filter(gender='Female').count()
    print(student_gender_female,student_gender_male)


    context = {
        'alumni_count': alumni_count,
        'event_count': event_count,
        'job_count': job_count,
    }
    return render(request, 'Staff/home.html',context)
    

@login_required(login_url='/')
def ADD_ALUMNI(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    
    
    if request.method == 'POST':
        profile_pic =request.FILES.get('profile_pic')
        first_name =request.POST.get('')
        last_name =request.POST.get('last_name')
        gender = request.POST.get('gender')
        email =request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password')
        course_id =request.POST.get('course_id')
        session_year_id =request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email is ALready Taken!')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already Taken!')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type= 2
            )

            user.set_password(password)
            user.save()
        
            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

            alumni = Alumni(
                admin = user,
                gender = gender,
                session_year_id = session_year,
                course_id= course,
                                
            )
            print(alumni)
            alumni.save()
            messages.success(request,user.first_name + ' '+ user.last_name + ' ' + 'Added Successfully!')
            return redirect('add_student')



            
    context = {
        'course': course,
        'session_year': session_year,
    }
    return render(request, 'Staff/add_student.html',context)


def EDIT_ALUMNI(request,id):
    alumni =Alumni.objects.filter(id =id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'alumni':alumni,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Staff/edit_alumni.html',context)

def UPDATE_ALUMNI(request):
    if request.method == 'POST':
        alumni_id = request.POST.get('alumni_id')
        profile_pic =request.FILES.get('profile_pic')
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        gender = request.POST.get('gender')
        email =request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password')
        course_id =request.POST.get('course_id')
        session_year_id =request.POST.get('session_year_id')

        user = CustomUser.objects.get(id =alumni_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        
        if password!=None and password != "":
              user.set_password(password)
        if profile_pic != None and profile_pic != "":
              user.profile_pic = profile_pic
        user.save()

        alumni = Alumni.objects.get(admin=alumni_id)
        alumni.gender= gender
        
        course = Course.objects.get(id = course_id)
        alumni.course_id =course

        session_year = Session_Year.objects.get(id = session_year_id)
        alumni.session_year_id=session_year

        alumni.save()
        messages.success(request,user.first_name + ' '+ user.last_name + ' ' + 'Record Are Successfully Updated!')
        return redirect('view_alumni')

        
    return render(request,'Staff/edit_alumni.html')


def DELETE_ALUMNI(request,admin):
    alumni = CustomUser.objects.get(id = admin)
    alumni.delete()
    messages.success(request, "Record Are Succesfully Deleted!")
    return redirect('view_alumni')



def ADD_EVENT(request):

    if request.method == 'POST':
        event_img =request.FILES.get('event_img')
        title =request.POST.get('Title')
        description =request.POST.get('description')
        try:
            event = Event(
                Title=title,
                event_img=event_img,
                description=description,
            )
            event.save()
            messages.success(request, 'Event Added Successfully!')
        except:
           messages.error(request,'Failed To Add Event!')
           return redirect('add_event')
    return render(request,'Staff/add_event.html')



