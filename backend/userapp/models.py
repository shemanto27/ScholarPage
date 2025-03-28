from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#1.---------------------------- Achievement Model
class Achievement(models.Model):
    achievement = models.CharField(max_length=150, unique=False, blank=True)
    def __str__(self):
        return self.achievement


#2.---------------------------- Education Model
class Education(models.Model):
    education = models.CharField(max_length=150, unique=False, blank=True)
    def __str__(self):
        return self.education

#3.---------------------------- Work Experience Model
class Work_Experience(models.Model):
    work_experience = models.CharField(max_length=150, unique=False, blank=True)
    def __str__(self):
        return self.work_experience

#4.---------------------------- Skills Model
class Skills(models.Model):
    skills = models.CharField(max_length=150, unique=False, blank=True)
    def __str__(self):
        return self.skills


#5.--------------- Research Interests Model
class Research_Interest(models.Model):
    research_interests = models.CharField(max_length=20, unique=False)

    def __str__(self):
        return self.research_interests



#6.---------------------------- Tag Model
class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=False)

    def __str__(self):
        return self.tag


#7.-------------------------------- Location Model
class Location(models.Model):
    location = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.location




#8.-------------------------------- User Model
class User(AbstractUser):
    GENDER_CHOICE = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]

    username = models.CharField(max_length=20, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=True)

    first_name = None
    last_name = None
    groups = None 
    user_permissions = None
    

    full_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='user_profile_pics/', blank=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICE, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True)
    work_experience = models.ManyToManyField(Work_Experience, blank=True)
    skills = models.ManyToManyField(Skills, blank=True)
    research_interest = models.ManyToManyField(Research_Interest, blank=True, related_name='users')
    publications = models.ManyToManyField('Publication',related_name='users', blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username' # The field to use as the unique identifier for authentication
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


#9.-------------------------------- Publication Model
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

    title = models.CharField(max_length=300, unique=False)
    publication_type = models.CharField(max_length=15,choices=PUBLICATION_TYPE_CHOICE, default='JOURNAL')
    tags = models.ManyToManyField(Tag, related_name='publications')
    description = models.TextField(max_length=250)
    status = models.CharField(max_length=15,default='PUBLISHED', choices=STATUS_CHOICE)
    published_year = models.DateField(blank=True, null=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title