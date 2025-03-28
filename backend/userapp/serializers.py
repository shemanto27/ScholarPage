from rest_framework import serializers

from .models import *

#1.---------------------------- User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'bio', 'profile_pic', 'gender', 'location', 'achievements', 'publications', 'research_interest', 'skills', 'work_experience', 'education']

#2.---------------------------- Achievement Serializer
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

#3.---------------------------- Publication Serializer
class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

#4.---------------------------- Location Serializer
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

#5.---------------------------- Tag Serializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#6.---------------------------- Research Interest Serializer
class ResearchInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research_Interest
        fields = '__all__'

#7.---------------------------- Skills Serializer
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

#8.---------------------------- Work Experience Serializer
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_Experience
        fields = '__all__'

#9.---------------------------- Education Serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
