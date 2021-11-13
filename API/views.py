from django.db.models.query import QuerySet
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Video
from .serializers import VideoSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .pagination import VideoPagination



import time 
from .key_query import key, query
import requests
import json
from dateutil import parser
import threading

# Create your views here.
def index(request):
    return HttpResponse("Server Working !!")

def update_table():
    while True : 
        time.sleep(20)
        try : 
            url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={key}"
            response = requests.request("GET", url, headers={}, data={})
            data = json.loads(response.text)
            for elem in data["items"]:
                if not Video.objects.filter(id = elem["id"]["videoId"]).exists():
                    video = Video(id = elem["id"]["videoId"],title = elem["id"]["videoId"],
                    description = elem["snippet"]["title"],publishing_date_time = parser.parse(elem["snippet"]["publishedAt"]),
                    thumbnail_URL = elem["snippet"]["thumbnails"]["default"]["url"])
                    video.save()
        except : 
            print("Error Occured")



class VideosView(viewsets.ModelViewSet):
    queryset = Video.objects.all() 
    pagination_class = VideoPagination
    serializer_class = VideoSerializer 
    http_method_names = ['get']
   
class VideoQuery(APIView):
    def get(self,request):
        if 'description' in list(request.data.keys()) and 'title' in list(request.data.keys()):
            return Response({
                "message" : "Specify Only One thing ! Either Description or Title"
            },status = status.HTTP_400_BAD_REQUEST)
        elif 'description' in list(request.data.keys()):
            videos = Video.objects.search_by_description(request.data["description"])
            serializer = VideoSerializer(videos, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        elif 'title' in list(request.data.keys()):
            videos = Video.objects.search_by_title(request.data["title"])
            serializer = VideoSerializer(videos, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response({
            "message" : "Neither of keys found description nor title"
        },status = status.HTTP_400_BAD_REQUEST)




t = threading.Thread(target=update_table)
t.start()