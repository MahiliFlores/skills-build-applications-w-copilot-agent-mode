import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request):
    codespace_name = os.environ.get("CODESPACE_NAME")

    base_url = f"https://{codespace_name}-8000.app.github.dev/api"

    return Response({
        "api_base_url": f"{base_url}/",
        "endpoints": [
            f"{base_url}/users/",
            f"{base_url}/teams/",
            f"{base_url}/activities/",
            f"{base_url}/workouts/",
            f"{base_url}/leaderboard/",
        ]
    })


urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.api_urls')),
]