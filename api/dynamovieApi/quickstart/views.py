# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dynamovieApi.MovieModel import MovieModel


@api_view(['GET', 'PUT', 'DELETE'])
def movies_list(request):
    """
    List movies
    """
    if request.method == 'GET':
        movie = MovieModel()
        json = movie.find_genre('ction')
        return Response(json)

    if request.method == 'DELETE':
        movie = MovieModel()
        json = movie.del_title('Furious 7')
        return Response(json)

    if request.method == 'PUT':
        movie = MovieModel()
        json = movie.add_movie('Spiderman Far From Home', 'Action', 'Disney', 'Unknown', 'Jake Gyllenhaal')
        return Response(json)
