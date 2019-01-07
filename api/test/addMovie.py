from dynamovieApi.MovieModel import MovieModel

movie = MovieModel("Furious 7", Genre="Action", Studio="Universal", Director="James Wan", Actor=["Jordana Brewster"])
movie.save()
