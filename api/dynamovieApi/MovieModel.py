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
        """
        Serialize filtered movie rows to json. ToDo: rewrite with Python's ORM interface
        """
        response = '{ "rows": ['
        rows_number = 0
        for column in self.scan(filtering):
            if rows_number > 0:
                response += ','
            rows_number += 1
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
        response += '],"rows_number": "' + str(rows_number) + '"}'
        return json.loads(response)

    def find(self, category, search):
        if len(search) > 0:
            if category == 'actor':
                return self.list(MovieModel.Actor.contains(search))
            if category == 'director':
                return self.list(MovieModel.Director.contains(search))
            if category == 'genre':
                return self.list(MovieModel.Genre.contains(search))
            if category == 'studio':
                return self.list(MovieModel.Studio.contains(search))
            if category == 'title':
                return self.list(MovieModel.Title.contains(search))
        return self.list(MovieModel.Title.exists())  # all movies
