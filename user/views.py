from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from user.serializers import UserSerializer, UserJWTSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserJWTSerializer


class ManageUserView(generics.RetrieveAPIView):
    serializer_class = UserJWTSerializer

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return get_user_model().objects.all()
        return get_user_model().objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        """Мені здалося дивним що вчителі можуть створювати учнів, тому тут заборонив POST"""
        return Response({"message": "POST method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff and instance.is_staff:
            return Response({"message": "You are not allowed to update other administrators."},
                            status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff and instance.is_staff:
            return Response(
                {"message": "You are not allowed to delete other administrators."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
