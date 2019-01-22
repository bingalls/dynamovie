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
    Genre = UnicodeAttribute()
    Studio = UnicodeAttribute()
    Director = UnicodeAttribute()
    Actor = UnicodeSetAttribute()

    def add_movie(self, title, genre, studio, director, actor):
        movie = MovieModel(title, genre)
        movie.save()
        return json.loads('{}')

    def del_title(self, title):
        print(title)
        self.delete(MovieModel.Title == title)
        return json.loads('{}')

    def list(self, filtering):
        response = '{ "rows": ['
        rowsNumber = 0
        for column in self.scan(filtering):
            if rowsNumber > 0:
                response += ','
            rowsNumber += 1
            # for actor in column.Actor: # return first actor, only
            #     break
            response += '{"title": "' + column.Title + \
                '", "genre": "' + column.Genre + \
                '", "studio": "' + column.Studio + \
                '", "director": "' + column.Director + \
                '", "actors": "'
            # '", "actor": "' + actor + '"}' + \
            for person in column.Actor:
                response += person + ';'
            response = response.strip(';') + '"}'
        response += '],"rowsNumber": "' + str(rowsNumber) + '"}'
        return json.loads(response)
        # return response
    
    def find_actor(self, actor=''):
        if len(actor) < 1:
            filtering = MovieModel.Actor.exists()
        else:
            filtering = MovieModel.Actor.contains(actor)
        return self.list(filtering)

    def find_director(self, director=''):
        if len(director) < 1:
            filtering = MovieModel.Director.exists()
        else:
            filtering = MovieModel.Director.contains(director)
        return self.list(filtering)

    def find_genre(self, genre=''):
        if len(genre) < 1:
            filtering = MovieModel.Genre.exists()
        else:
            filtering = MovieModel.Genre.contains(genre)
        return self.list(filtering)

    def find_studio(self, studio=''):
        if len(studio) < 1:
            filtering = MovieModel.Studio.exists()
        else:
            filtering = MovieModel.Studio.contains(studio)
        return self.list(filtering)

    def find_title(self, title=''):
        if len(title) < 1:
            filtering = MovieModel.Title.exists()
        else:
            filtering = MovieModel.Title.contains(title)
        return self.list(filtering)
