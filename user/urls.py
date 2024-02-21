from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import (
    CreateUserView,
    ManageUserView,
    UserViewSet
)

router = routers.DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("me/", ManageUserView.as_view(), name="me"),
    path("", include(router.urls)),
]

app_name = "user"
