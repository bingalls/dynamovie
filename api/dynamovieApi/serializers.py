from dynamovieApi.MovieModel import MovieModel
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieModel
        fields = ('Title', 'Genre', 'Studio', 'Director', 'Actor')

