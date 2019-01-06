from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UnicodeSetAttribute
import json


# noinspection PyUnusedName
class MovieModel(Model):
    """
    A DynamoDB Movie collection
    Tested on localhost. Remove `host` if you use AWS
    """

    # noinspection PyUnusedClass,PyUnusedName
    class Meta:
        table_name = "Movies"
        host = "http://localhost:8000"
    Title = UnicodeAttribute(hash_key=True)
    Genre = UnicodeAttribute(range_key=True)
    Studio = UnicodeAttribute(null=True)
    Director = UnicodeAttribute(null=True)
    Actor = UnicodeSetAttribute()

    def add_movie(self, title, genre, studio, director, actor):
        movie = MovieModel(title, genre)
        movie.save()
        return json.loads('{}')

    # FIXME static?
    def del_title(self, title):
        MovieModel.delete(MovieModel.Title.__eq__(title))
        return json.loads('{}')

    def list(self, filtering):
        response = '{ "data": ['
        rowsNumber = 0
        for column in self.scan(filtering):
            if rowsNumber > 0:
                response += ','
            rowsNumber += 1
            for actor in column.Actor: # return first actor, only
                break
            response += '{"title": "' + column.Title + \
                '", "genre": "' + column.Genre + \
                '", "studio": "' + column.Studio + \
                '", "director": "' + column.Director + \
                '", "actor": "' + actor + '"}'
            #     '", "actors": ['
            # for person in column.Actor:
            #     response += '"' + person + '",'
            # response = response.strip(',') + ']}'
        response += '],"rowsNumber":' + str(rowsNumber) + '}'
        return json.loads(response)
    
    def find_genre(self, genre=''):
        if len(genre) < 1:
            filtering = MovieModel.Genre.exists()
        else:
            filtering = MovieModel.Genre.contains(genre)
        return self.list(filtering)

    def find_title(self, title=''):
        if len(title) < 1:
            filtering = MovieModel.Title.exists()
        else:
            filtering = MovieModel.Title.contains(title)
        return self.list(filtering)
