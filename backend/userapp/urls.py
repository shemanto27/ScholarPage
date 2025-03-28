from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

# 1. User Router
router.register(r'users', UserViewSet)

# 2. Achievement Router
router.register(r'achievements', AchievementViewSet)

# 3. Publication Router
router.register(r'publications', PublicationViewSet)

# 4. Location Router
router.register(r'locations', LocationViewSet)

# 5. Tag Router
router.register(r'tags', TagViewSet)

# 6. Research Interest Router
router.register(r'research_interests', ResearchInterestViewSet)

# 7. Education Router
router.register(r'educations', EducationViewSet)

# 8. Experience Router
router.register(r'experiences', ExperienceViewSet)

# 9. Skill Router
router.register(r'skills', SkillsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]