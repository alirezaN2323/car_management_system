from django.urls import path
from .views import OwnerListAPIView, OwnerDetailAPIView

app_name = 'owners'

urlpatterns = [
    path('list/', OwnerListAPIView.as_view()),
    path('detail/', OwnerDetailAPIView.as_view()),
]

