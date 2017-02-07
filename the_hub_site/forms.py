from django.contrib import admin
from django import forms
from .models import Semester, Projects

class ProjectsAdminForm(forms.ModelForm):
    semester_to_projects = forms.ModelMultipleChoiceField(
        Semester.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple('Semester', False),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(ProjectsAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['semester_to_projects'] = self.instance.semester_to_projects.values_list('pk', flat=True)

    def save(self, *args, **kwargs):
        instance = super(ProjectsAdminForm, self).save(*args, **kwargs)
        if instance.pk:
            instance.semester_to_projects.clear()
            instance.semester_to_projects.add(*self.cleaned_data['semester_to_projects'])
        return instance

class MembersAdminForm(forms.ModelForm):
    semesters_to_members = forms.ModelMultipleChoiceField(
        Semester.objects.all(),
        widget = admin.widgets.FilteredSelectMultiple('Semesters', False),
        required=False,
    )
    
    projects_to_members = forms.ModelMultipleChoiceField(
        Projects.objects.all(),
        widget = admin.widgets.FilteredSelectMultiple('Projects', False),
        required=False,
    )
    
    def __init__(self, *args, **kwargs):
        super(MembersAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['semesters_to_members'] = self.instance.semesters_to_members.values_list('pk', flat=True)
            self.initial['projects_to_members'] = self.instance.projects_to_members.values_list('pk', flat=True)
    
    def save(self, *args, **kwargs):
        instance = super(MembersAdminForm, self).save(*args, **kwargs)
        if instance.pk:
            instance.semesters_to_members.clear()
            instance.projects_to_members.clear()
            instance.semesters_to_members.add(*self.cleaned_data['semesters_to_members'])
            instance.projects_to_members.add(*self.cleaned_data['projects_to_members'])
        return instance
    