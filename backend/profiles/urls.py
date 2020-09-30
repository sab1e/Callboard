from django.urls import path

from .views import ProfileDetail


urlpatterns = [
    path('<int:pk>', ProfileDetail.as_view(), name='profile-detail')
]
