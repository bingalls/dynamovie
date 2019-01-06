from dynamovieApi.MovieModel import MovieModel

movie = MovieModel("Furious 7", "Action")
movie.Studio = "Universal"
movie.Director = "James Wan"
movie.Actor = ["Jordana Brewster"]
movie.save()
