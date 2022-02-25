from django.urls import path
from .views import TollStationListAPIView

app_name = 'toll_stations'

urlpatterns = [
    path('list/', TollStationListAPIView.as_view()),
]