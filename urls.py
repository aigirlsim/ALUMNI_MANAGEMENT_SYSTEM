
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import Staff_views, alumni_views, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name ='base'),


    #Login Path
    path('', views.LOGIN, name ='login'),
    path('dologin',views.dologin, name='dologin'),
    path('dologout',views.dologout, name='logout'),

    #profile update
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    path ('View',views.VIEW_ALUMNI,name ='view_alumni'),

    #This is staff panel
    path ('Staff/Home',Staff_views.HOME,name ='staff_home'),
    path ('Staff/Student/Add',Staff_views.ADD_ALUMNI,name ='add_student'),
    path ('Staff/Student/Edit/<str:id>',Staff_views.EDIT_ALUMNI,name ='edit_alumni'),
    path ('Staff/Student/update',Staff_views.UPDATE_ALUMNI,name ='update_alumni'),
    path ('Staff/Student/Delete/<str:admin>',Staff_views.DELETE_ALUMNI,name ='delete_alumni'),
    path ('Staff/Student/Add_Event',Staff_views.ADD_EVENT,name ='add_event'),
    


#This is Alumni panel
path ('Alumni/Home',alumni_views.HOME,name ='alumni_home'),
path ('Alumni/Post',alumni_views.POSTJOB,name ='post_job'),
path ('Alumni/Post_save',alumni_views.SAVE_JOB,name ='post_job_save'),
path ('Alumni/view_job',alumni_views.VIEW_JOB,name ='view_job'),
path('Alumni/view_events',alumni_views.VIEW_EVENTS,name='view_events'),




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

