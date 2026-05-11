
import os
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.http import JsonResponse
from django.conf import settings


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

# Middleware-like function to inject API base URL in root endpoint
def api_root_with_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({
        "api_base_url": base_url,
        "endpoints": [
            f"{base_url}users/",
            f"{base_url}teams/",
            f"{base_url}activities/",
            f"{base_url}workouts/",
            f"{base_url}leaderboard/",
        ]
    })

urlpatterns = [
    path('', api_root_with_base_url, name='api-root'),
]
urlpatterns += router.urls
