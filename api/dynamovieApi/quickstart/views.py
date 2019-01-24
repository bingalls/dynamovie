from rest_framework.decorators import api_view
from rest_framework.response import Response
from dynamovieApi.MovieModel import MovieModel


@api_view(['DELETE', 'GET', 'POST', 'PUT'])
def movies_list(request):
    """
    List movies
    """
    if request.method == 'GET':
        category = ''
        movie = MovieModel()
        search = ''
        if request.GET.__contains__('cat'):
            category = request.GET.__getitem__('cat')
        if request.GET.__contains__('search'):
            search = request.GET.__getitem__('search')
        return Response(movie.find(category, search))

    if request.method == 'DELETE':
        movie = MovieModel()
        json = movie.del_title('Furious 7')
        return Response(json)

    if request.method == 'PUT':
        movie = MovieModel()
        json = movie.add_movie('Spiderman Far From Home', 'Action', 'Disney', 'Unknown', 'Jake Gyllenhaal')
        return Response(json)
