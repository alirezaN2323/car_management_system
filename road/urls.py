from django.urls import path
from .views import RoadListAPIView, RoadDetailAPIView

app_name = 'roads'

urlpatterns = [
    path('list/', RoadListAPIView.as_view()),
    path('detail/<int:pk>/', RoadDetailAPIView.as_view()),
]