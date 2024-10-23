# users/urls.py

from django.urls import path, include
from .views import UserRegistrationView, UserListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('accounts/', include('allauth.urls')),
]



