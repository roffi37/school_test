from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/event/", include("event.urls", namespace="event")),
    path("api/user/", include("user.urls", namespace="user")),
]
