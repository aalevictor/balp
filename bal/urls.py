from django.urls import path

from bal.views import PlayersAPI

urlpatterns = [
    path('players', PlayersAPI.as_view(), name='Players'),
    path('players/<str:uid>', PlayersAPI.as_view(), name='Players'),
]
