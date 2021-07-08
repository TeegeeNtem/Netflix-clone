from rest_framework import viewsets

from .models import Movie, TvShow, Episode, Video
from .serializers import MovieSerializer, TvShowSerializer
from .serializers import EpisodeSerializer, VideoSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TvShowViewSet(viewsets.ModelViewSet):
    queryset = TvShow.objects.all()
    serializer_class = TvShowSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer 
