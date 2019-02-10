"""API for a single movie."""
from dynamovieApi.MovieModel import MovieModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from simplejson import loads
import bleach


@api_view(['DELETE', 'GET'])
def handle(request, title):
    """Process a movie by its title."""
    title = bleach.clean(title)

    if request.method == 'GET':
        movie = MovieModel()
        return Response(movie.find('title', title))

    if request.method == 'DELETE':
        movie = MovieModel()
        return Response(movie.del_title(title))

    return loads('{}')  # other http method should not be allowed
