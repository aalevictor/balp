from django.urls import path

from ocr.views import PerksAPI

urlpatterns = [
    path('perks', PerksAPI.as_view(), name='Perks'),
]
