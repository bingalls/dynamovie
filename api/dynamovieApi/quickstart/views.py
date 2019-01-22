from rest_framework.decorators import api_view
from rest_framework.response import Response
from dynamovieApi.MovieModel import MovieModel


@api_view(['DELETE', 'GET', 'POST', 'PUT'])
def movies_list(request):
    """
    List movies
    """
    if request.method == 'GET':
        movie = MovieModel()
        if request.GET.__contains__('col') and request.GET.__contains__('search'):
            col = request.GET.__getitem__('col')
            search = request.GET.__getitem__('search')
            if col == 'actor':
                json = movie.find_actor(search)
            elif col == 'director':
                json = movie.find_director(search)
            elif col == 'genre':
                json = movie.find_genre(search)
            elif col == 'studio':
                json = movie.find_studio(search)
            elif col == 'title':
                json = movie.find_title(search)
            else:
                json = movie.find_genre() # list all movies
        else:
            json = movie.find_genre()
        return Response(json)

    if request.method == 'DELETE':
        movie = MovieModel()
        json = movie.del_title('Furious 7')
        return Response(json)

    if request.method == 'PUT':
        movie = MovieModel()
        json = movie.add_movie('Spiderman Far From Home', 'Action', 'Disney', 'Unknown', 'Jake Gyllenhaal')
        return Response(json)
