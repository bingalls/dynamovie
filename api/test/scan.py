from dynamovieApi.MovieModel import MovieModel


def scan():
    response = "{"
    clean = True
    # for column in MovieModel.scan(MovieModel.Genre.contains(genre)):
    for column in MovieModel.scan():
        if clean:
            response += ",\n"
        clean = False
        response += '["title": "' + column.Title + \
            '", "genre": "' + column.Genre +\
            '", "studio": "' + column.Studio + \
            '", "director": "' + column.Director + \
            '", "actors": ['
        for person in column.Actor:
            response += '"' + person + '",'

    # print(response)
    response = response.strip(',') + ']]'
    response += '}'
    return response


print(scan())
