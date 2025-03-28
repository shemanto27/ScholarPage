from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.

# 1. User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 2. Achievement ViewSet
class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

# 3. Publication ViewSet
class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

# 4. Location ViewSet
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# 5. Tag ViewSet
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# 6. Research Interest ViewSet
class ResearchInterestViewSet(viewsets.ModelViewSet):
    queryset = Research_Interest.objects.all()
    serializer_class = ResearchInterestSerializer

# 7. Education ViewSet
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

# 8. Experience ViewSet
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Work_Experience.objects.all()
    serializer_class = WorkExperienceSerializer

# 9. Skill ViewSet
class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer



