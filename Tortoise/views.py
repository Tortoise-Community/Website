from django.shortcuts import render , HttpResponse,redirect
from websitedata.models import *
from .oauth import Oauth
from userdata.models import Members




# Create your views here.


def get_event(request, item_name):
    E = Events.get(pk = item_name)
    return render(request, 'event.html', {'E':E,'Team':Team})

def get_project(request,item_name):
    P = Projects.get(pk = item_name)
    return render(request,'project.html',{'P':P,'Team':Team})   
    
Slides = Slider.objects.all()
News = News.objects.all()
Team = Team.objects.all()
Upcoming = Events.objects.filter(status='Upcoming')
RecEvents = Events.objects.filter(status='Ended').order_by('enddate')[:3]
LiveEvents = Events.objects.filter(status='Live')
Events = Events.objects.filter(status__in=['Live','Ended'])
Projects = Projects.objects.all()
Members = Members.objects.all().order_by('perks')[:10]

def index(request):
    return render(request,"index.html",{'Slides':Slides,'News':News,'Team':Team,'Upcoming':Upcoming,'RecEvents':RecEvents,'Projects':Projects,'LiveEvents':LiveEvents})

def projects(request):
    return render(request,"projects.html",{'Team':Team,"Projects" : Projects})    

def events(request):
    return render(request,"events.html",{'Events':Events,'Team':Team,'Upcoming':Upcoming})        
    
def verify(request):
    return render(request,"verification.html",{'Oauth':Oauth})        

def contact(request):
    return render(request,"contact.html",{'Team':Team})     


def event(request):
    return render(request,"event.html",{'Team':Team})      


def vamp(request):
    return render(request,"event.html",{"E":E,'Team':Team})                

def verified(request):
    code = request.GET.get("code")
    access_token = Oauth.get_access_token(code)
    user_json = Oauth.get_user_json(access_token)
    username = user_json.get("email")   
    Verified = True
    id = user_json.get("id")   
    if id is None :
        return render(request,"verification.html",{'Oauth':Oauth})
    else :  
        return render(request,"verification.html",{'Verified':Verified})  

def members(request):
    return render(request,"members.html",{'Team':Team,'Members':Members})    

def credits(request):
    return render(request,"credits.html")       

def announcements(request):
    return render(request,"announcements.html")       

def x(request):
    res = Members.objects.all()
    return HttpResponse(res)