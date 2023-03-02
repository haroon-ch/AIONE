from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from ytDownloader import views as yt_v
from aione import views as aione_v
from converter import views as co_v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('YT-Video', yt_v.ytd, name="ytd"),
    # path('index', dom_v.homep),
    path('', aione_v.homep),
    path('aione-services', aione_v.aiservice, name="aione-services"),
    path('aione-contact-us', aione_v.aicontact, name="aione-contact-us"),
    path('aione-about-us', aione_v.aiabout, name="aione-about-us"),
    path('Aione-Home', aione_v.aione, name="Aione-Home"),
    path('Video-Details', co_v.videodetails, name="Video-Details"),
    path('video-to-audio', co_v.downloadmp3, name="video-to-audio"),
    path('video2audio', co_v.video2audio, name="video2audio"),
    path('downloadmp3', co_v.downloadmp3, name="downloadmp3"),
    # domain checker
    # path('domain-informations', do_v.domain, name="domain-informations"),

	path('download/', yt_v.download_page, name="download"),
	path('download/<res>/', yt_v.success, name="success"),
    path('', include('ytDownloader.urls')),
    path('', include('converter.urls')),
    # path('', include('doinf.urls')),
]

