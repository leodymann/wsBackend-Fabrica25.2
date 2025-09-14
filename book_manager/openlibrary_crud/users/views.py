from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class RegisterUserAPIView(generics.CreateAPIView):
    # api for register new users
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
