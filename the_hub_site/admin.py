from django.contrib import admin
from .models import Member, Semester, Projects
from .forms import ProjectsAdminForm, MembersAdminForm

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    #list_display = ['name', 'role']
    form = MembersAdminForm

class SemesterAdmin(admin.ModelAdmin):
    list_display = ['year', 'season']
    
class ProjectsAdmin(admin.ModelAdmin):
    #list_display = ['name', 'description']
    form = ProjectsAdminForm

admin.site.register(Member, MemberAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Projects, ProjectsAdmin)

