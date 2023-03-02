from django.urls import path
from . import views

urlpatterns = [
    path('check-videodetails', views.home, name="check-videodetails"),
    path('video-to-audio', views.downloadmp3, name="video-to-audio"),
    path('downloadmp3', views.downloadmp3, name="Downloadmp3"),
    path('downloadmp4', views.downloadmp4, name="Downloadmp4"),
    path('videodetails', views.videodetails, name="videodetails"),
    path('onlineaudio', views.videodetails, name="videodetails")
    
]