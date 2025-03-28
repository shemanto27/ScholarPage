from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#--------------- Research Interests Model
class Research_Interest(models.Model):
    research_interests = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.research_interests



#---------------------------- Tag Model
class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tag


#-------------------------------- Location Model
class Location(models.Model):
    location = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.location




#-------------------------------- User Model
class User(AbstractUser):
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    full_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='user_profile_pics/', blank=True)
    location = models.ManyToManyField(Location, blank=True)
    gender = models.CharField(max_length=15,choices=GENDER_CHOICE, blank=True)
    education = models.CharField(max_length=50, blank=True)
    achievements = models.CharField(max_length=50, blank=True)
    work_experience = models.CharField(max_length=50, blank=True)
    research_interest = models.ManyToManyField(Research_Interest, blank=True, related_name='users')
    skilled_with = models.CharField(max_length=50, blank=True)
    publications = models.ManyToManyField('Publication', related_name='users')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


#-------------------------------- Publication Model
class Publication(models.Model):
    STATUS_CHOICE = [
        ('PUBLISHED', 'Published'),
        ('WORKING ON IT', 'Working on it'),
        ('SUBMITTED', 'Submitted'),
        ('DISCONTINUED', 'Discontinued'),
    ]

    PUBLICATION_TYPE_CHOICE = [
        ('JOURNAL', 'Journal'),
        ('CONFERENCE', 'Conference'),
        ('BOOK', 'Book'),
        ('THESIS', 'Thesis'),
        ('PROJECT', 'Project'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=300)
    authors = models.ManyToManyField(User, related_name='authors')
    publication_type = models.CharField(max_length=15,choices=PUBLICATION_TYPE_CHOICE, default='JOURNAL')
    tags = models.ManyToManyField(Tag, related_name='publications')
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=15,default='PUBLISHED', choices=STATUS_CHOICE)
    published_year = models.DateField(blank=True, null=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title