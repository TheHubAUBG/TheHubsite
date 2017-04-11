from django.shortcuts import render
from .models import Events, Member, Projects, Semester
# Create your views here.

def index(request):
    events = Events.objects.all()
    members = Member.objects.all()
    projects = Projects.objects.all()
    semesters = Semester.objects.all()
    context = {'events': events, 'members': members, 'projects': projects, 'semesters': semesters}
    return render(request, 'the_hub_site/index.html', context)


