from django.urls import path

from accounts.views import UsersAPI

urlpatterns = [
    path('register', UsersAPI.as_view(), name='Users')
]
