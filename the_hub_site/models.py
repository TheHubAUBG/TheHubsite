from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Member(models.Model):
    picture = models.ImageField(blank=True)
    name = models.CharField(max_length=120)
    role = models.TextField()
    
    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    members_to_projects = models.ManyToManyField(Member,
                                                 related_name='projects_to_members',
                                                 blank=True)
    
    def __str__(self):
        return "{}: {}".format(self.name, self.description)
    
class Semester(models.Model):
    YEAR_CHOICES = [(r,r) for r in range(2014, datetime.date.today().year+1)]
    
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    season = models.CharField(max_length=50)
    members_to_semesters = models.ManyToManyField(Member, 
                                                 related_name='semesters_to_members',
                                                 blank=True)
    
    projects_to_semester = models.ManyToManyField(Projects,
                                                  related_name='semester_to_projects',
                                                  blank=True)
    
    def __str__(self):
        return "{} semester, {}".format(self.season, self.year)
    
    class Meta:
        ordering = ('-year',)
        
class Events(models.Model):
    TYPE_CHOICES = (
        ('field_trip','Field Trip'),
        ('presentation', 'Presentation'),
        ('workshop', 'Workshop'),    
    )
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    )
    
    name = models.CharField(max_length=70)
    type = models.CharField(max_length=14,
                            choices=TYPE_CHOICES,
                            default='presentation')
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=300)
    presenters = models.CharField(max_length=150)
    level = models.CharField(max_length=14,
                             choices=LEVEL_CHOICES,
                             default='beginner')
    target_audience = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name