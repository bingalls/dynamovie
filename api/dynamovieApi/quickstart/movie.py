from dynamovieApi.MovieModel import MovieModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from simplejson import loads
import bleach


@api_view(['DELETE', 'GET'])
def movie_get(request, title):
    if request.method == 'GET':
        movie = MovieModel()
        return Response(movie.find('title', bleach.clean(title)))

    if request.method == 'DELETE':
        movie = MovieModel()
        return Response(movie.del_title(bleach.clean(title)))

    return loads('{}')  # other http method should not be allowed
