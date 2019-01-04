from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dynamovieApi.MovieModel import MovieModel


@api_view(['GET', 'PUT', 'DELETE'])
def movies_list(request):
    """
    List movies
    """
    if request.method == 'GET':
        json = MovieModel.findGenre('Fiction')
        return Response(json)
