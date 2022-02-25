from django.urls import path
from .views import AllNodeListAPIView, AllNodeDetailAPIView

app_name = 'road_tables'

urlpatterns = [
    path('list/', AllNodeListAPIView.as_view()),
    path('detail/<int:pk>', AllNodeDetailAPIView.as_view())
]

