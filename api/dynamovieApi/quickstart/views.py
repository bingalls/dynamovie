"""Route Movies requests."""
from dynamovieApi.MovieModel import MovieModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from simplejson import loads
import bleach


@api_view(['DELETE', 'GET', 'POST', 'PUT'])
def movies_list(request):
    """List movies."""
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
        category = parameters.get('category', '')
        search = parameters.get('search', '')
        title = parameters.get('title', '')
        movie = MovieModel(title)
        return Response(movie.del_title(title, category, search))

    if request.method == 'POST':
        parameters = loads(bleach.clean(request.body.decode("utf-8")))
        actor = parameters.get('actors', '')
        category = parameters.get('category', '')
        director = parameters.get('director', '')
        genre = parameters.get('genre', '')
        search = parameters.get('search', '')
        newtitle = parameters.get('newtitle', '')
        oldtitle = parameters.get('oldtitle', '')
        studio = parameters.get('studio', '')
        movie = MovieModel(oldtitle)
        return Response(movie.edit_movie(oldtitle, genre, studio, director,
                        actor, newtitle, category, search))

    if request.method == 'PUT':
        parameters = loads(bleach.clean(request.body.decode("utf-8")))
        actors = parameters.get('actors', '')
        category = parameters.get('category', '')
        director = parameters.get('director', '')
        genre = parameters.get('genre', '')
        search = parameters.get('search', '')
        studio = parameters.get('studio', '')
        title = parameters.get('title', '')
        movie = MovieModel()
        return Response(movie.add_movie(title, genre, studio, director, actors,
                        category, search))

    return loads('{}')  # other http method should not be allowed
