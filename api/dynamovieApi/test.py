# noinspection PyUnresolvedReferences
from MovieModel import MovieModel

movie = MovieModel("Furious 7", "Action")
# movie.Studio = "Universal"
# movie.Director = "James Wan"
# movie.Actor = ["Jordana Brewster"]
# movie.save()

# movie = MovieModel()
# movie.del_title("Furious 7")

print(movie.find_genre())
# print(movie.find_genre('Science Fiction'))
