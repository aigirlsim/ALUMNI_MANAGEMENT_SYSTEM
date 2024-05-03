from django.shortcuts import render,redirect
from app.models import PJob,Event
from django.contrib import messages

def HOME(request):
    return render(request, 'Alumni/home.html')


def POSTJOB(request):
    return render(request, 'Alumni/post_job.html')


def SAVE_JOB(request):
    if request.method == 'POST':
        Title = request.POST.get('Title')
        company_name = request.POST.get('company_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        application_deadline = request.POST.get('application_deadline')
        apply_link = request.POST.get('apply_link')
        # print(Title,company_name,description,location,application_deadline,Link)
        job = PJob(
                Title=Title,
                CompanyName=company_name,
                description=description,
                Location=location,
                AplicvationDeadline=application_deadline,
                Link=apply_link,
            )
        
        job.save()
        messages.success(request, 'Job Added Successfully!')
   
        return redirect('post_job')
    
    
def VIEW_JOB(request):
    jobs = PJob.objects.all()

    context = {
        'jobs': jobs,
    }
    return render(request,'Alumni/view_job.html',context)
            


def VIEW_EVENTS(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }
    return render(request,'Alumni/view_events.html',context)          