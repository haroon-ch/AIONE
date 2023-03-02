from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from os.path import exists
import time
import os
import re
from django.http import JsonResponse
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import request


# Create your views here.
def home(request):
    return render(request, 'video-deatils.html')

def video2audio(request):
    return render(request, 'video2audio.html')


def clearolderfiles(path):
    deletepath = "media\\"+path
    if exists(deletepath):
        for folder in os.listdir(deletepath):
            modifiedtime = os.path.getmtime(
                os.path.abspath(deletepath+"\\"+folder))
            if time.time()-modifiedtime > 300:
                for file in os.listdir(deletepath+"\\"+folder):
                    os.remove(os.path.abspath(
                        deletepath+"\\"+folder+"\\"+file))
                os.rmdir(os.path.abspath(deletepath+"\\"+folder))

def downloadmp3(request):
    
    clearolderfiles("audiofiles")    
    # url input from user    
    #print("URL>>"+request.POST["address"])
    my_new_path ="media\\audiofiles\\"+re.sub('[^a-zA-Z0-9 \n\.]', '', request.POST["address"])
    if exists(my_new_path):          
        for file in os.listdir(my_new_path):
            if file.endswith(".mp3"):
                    audiofile = open(my_new_path+"\\"+file, "rb").read() 
                    response = HttpResponse(audiofile, content_type='audio/mpeg')
                    response['Content-Disposition'] = 'attachment; filename=' + file
    else:
        #print('Starting Conversion>>')
        yt = YouTube(str(request.POST["address"]))
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        # download the file        
        out_file = video.download(output_path=my_new_path)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'        
        os.rename(out_file, new_file)
        # result of success
        # print(yt.title + " has been successfully downloaded.")
        for file in os.listdir(my_new_path):
            if file.endswith(".mp3"):
                    audiofile = open(my_new_path+"\\"+file, "rb").read() 
                    response = HttpResponse(audiofile, content_type='audio/mpeg')
                    response['Content-Disposition'] = 'attachment; filename=' + file
    return response

def downloadmp4(request):
    clearolderfiles("videofiles")
    my_new_path = "media\\videofiles\\" + \
        re.sub('[^a-zA-Z0-9 \n\.]', '', request.POST["addressmp4"])
    if exists(my_new_path):
        for file in os.listdir(my_new_path):
            if file.endswith(".mp4"):
                audiofile = open(my_new_path+"\\"+file, "rb").read()
                response = HttpResponse(
                    audiofile, content_type='application/vnd.mp4')
                response['Content-Disposition'] = 'attachment; filename=' + file
    else:
        yt = YouTube(str(request.POST["addressmp4"]))
        video = yt.streams.get_highest_resolution()
        # download the file
        out_file = video.download(output_path=my_new_path)
        for file in os.listdir(my_new_path):
            if file.endswith(".mp4"):
                audiofile = open(my_new_path+"\\"+file, "rb").read()
                response = HttpResponse(
                    audiofile, content_type='application/vnd.mp4')
                response['Content-Disposition'] = 'attachment; filename=' + file
    return response


def videodetails(request):

    myVideo = YouTube(str(request.POST["details"]))
    return JsonResponse(
        {'vtitle': myVideo.title,
         'vlength': str(myVideo.length),
         'vthumburl': myVideo.thumbnail_url,
         'vdesc': myVideo.description,
         'vviews': str(myVideo.views),
         'vage': str(myVideo.age_restricted),
         'vvid': str(myVideo.video_id)
         })
