from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/me/', views.UserDetailView.as_view(), name='user-detail'),
    # Si necesitas endpoints adicionales para autenticación
    # path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path('profile/', views.UserProfileView.as_view(), name='profile'),
]