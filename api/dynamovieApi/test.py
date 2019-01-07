# noinspection PyUnresolvedReferences
from MovieModel import MovieModel

movie = MovieModel("Furious 7", Genre="Action", Studio="Universal", Director="James Wan", Actor=["Jordana Brewster"])
movie.save()


# movie = MovieModel.get("Furious 7", "Action")
# movie.delete()
# movie.del_title("Furious 7")

# print(movie.find_genre())
# print(movie.find_genre('Science Fiction'))
