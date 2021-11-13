from django.db import models


class VideoManager(models.Manager):
    def search_by_description(self,query):
        query = query.lower()
        videos = Video.objects.all()
        filtered_videos = [video for video in videos if query in video.description.lower()]
        return filtered_videos

    def search_by_title(self,query):
        query = query.lower()
        videos = Video.objects.all()
        filtered_videos = [video for video in videos if query in video.title.lower()]
        return filtered_videos

    

class Video(models.Model):
    id = models.CharField(primary_key=True,max_length=100,null = False,blank=False)
    title = models.CharField(max_length=100,null = False, blank = False)
    description = models.TextField(null = True, blank = True)
    publishing_date_time = models.DateTimeField(null = False, blank = False)
    thumbnail_URL = models.URLField(max_length=500,null =False, blank = False)

    objects = VideoManager()




