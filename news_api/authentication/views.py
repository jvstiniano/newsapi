from rest_framework import generics, permissions, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer
from .permissions import IsEditor

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    allowed_methods = ('POST')
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)

class UserListView(generics.ListAPIView):
    allowed_methods = ('GET')
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsEditor]
    required_scopes = ['read']

class UserDetailView(generics.RetrieveUpdateAPIView):
    allowed_methods = ('GET', 'PUT')
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['read']

    def get_object(self):
        return self.request.user