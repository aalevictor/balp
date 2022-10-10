from django.urls import path

from bal.views import PerksAPI, PlayersAPI

urlpatterns = [
    path('players', PlayersAPI.as_view(), name='Players'),
    path('players/<str:uid>', PlayersAPI.as_view(), name='Players'),
    path('perks', PerksAPI.as_view(), name='Perks'),
]
