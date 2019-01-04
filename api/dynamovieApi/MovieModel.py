from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UnicodeSetAttribute
import json

# Tested on localhost. Remove `host` if you use AWS
class MovieModel(Model):
    """
    A DynamoDB Movie collection
    """
    class Meta:
        table_name = "Movies"
        host = "http://localhost:8000"
    Title = UnicodeAttribute(hash_key=True)
    Genre = UnicodeAttribute(range_key=True)
    Studio = UnicodeAttribute(null=True)
    Director = UnicodeAttribute(null=True)
    Actor = UnicodeSetAttribute()

    def findGenre(genre):
        response = '{ "list": ['
        clean = True
        for column in MovieModel.scan(MovieModel.Genre.contains(genre)):
            if clean:
                clean = False
            else:
                response += ','

            response += '{"title": "' + column.Title + \
                    '", "genre": "' + column.Genre + \
                    '", "studio": "' + column.Studio + \
                    '", "director": "' + column.Director + \
                    '", "actors": ['
            for person in column.Actor:
                response += '"' + person + '",'

            response = response.strip(',') + ']}'
        response += ']}'
        return json.loads(response)
