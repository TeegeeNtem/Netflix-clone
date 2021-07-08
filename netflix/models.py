from django.db import models

class Video(models.Model):
    duration = models.TimeField()
    type = models.CharField(max_length=64, default='video/mp4')
    hd = models.BooleanField(default=False)
    path = models.CharField(max_length=1024)
    def __str__(self):
        return self.path

class Subtitle(models.Model):
    video = models.ForeignKey(Video, related_name='subtitles', on_delete=models.CASCADE)
    language = models.CharField(max_length=8, default='en-us')
    path = models.CharField(max_length=1024)
    def __str__(self):
        return self.path

class Movie(models.Model):
    title = models.CharField(max_length=512)
    release_date = models.DateField()
    content_rating = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters', max_length=512)
    video = models.ForeignKey(Video, on_delete=models.CASCADE )
    def __str__(self):
        return self.title

class TvShow(models.Model):
    title = models.CharField(max_length=512)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    content_rating = models.CharField(max_length=16)
    description = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters', max_length=512)
    def __str__(self):
        return self.title

class Episode(models.Model):
    tv_show = models.ForeignKey(TvShow, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    air_date = models.DateField()
    episode_num = models.SmallIntegerField()
    season_num = models.SmallIntegerField()
    description = models.TextField(blank=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
