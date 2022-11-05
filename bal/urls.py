from django.urls import path

from bal.views import PerksAPI, PlayersAPI, PlayersCSV

urlpatterns = [
    path('players', PlayersAPI.as_view(), name='Players'),
    path('player/<str:uid>', PlayersAPI.as_view(), name='Players'),
    path('import', PlayersCSV.as_view(), name='Import Players'),
    path('perks', PerksAPI.as_view(), name='Perks'),
]
