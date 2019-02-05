from dynamovieApi.MovieModel import MovieModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from simplejson import loads
import bleach


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
            category = bleach.clean(request.GET.__getitem__('cat'))
        if request.GET.__contains__('search'):
            search = bleach.clean(request.GET.__getitem__('search'))
        return Response(movie.find(category, search))

    if request.method == 'DELETE':
        parameters = loads(bleach.clean(request.body.decode("utf-8")))
        title = parameters.get('title', '')
        movie = MovieModel(title)
        return Response(movie.del_title(title))

    if request.method == 'POST':
        parameters = loads(bleach.clean(request.body.decode("utf-8")))
        actor = parameters.get('actors', '')
        director = parameters.get('director', '')
        genre = parameters.get('genre', '')
        studio = parameters.get('studio', '')
        oldtitle = parameters.get('oldtitle', '')
        newtitle = parameters.get('newtitle', '')
        movie = MovieModel(oldtitle)
        return Response(movie.edit_movie(oldtitle, genre, studio, director, actor, newtitle))

    if request.method == 'PUT':
        parameters = loads(bleach.clean(request.body.decode("utf-8")))
        actor = parameters.get('actors', '')
        director = parameters.get('director', '')
        genre = parameters.get('genre', '')
        movie = MovieModel()
        studio = parameters.get('studio', '')
        title = parameters.get('title', '')
        return Response(movie.add_movie(title, genre, studio, director, actor))

    return loads('{}')  # other http method should not be allowed
