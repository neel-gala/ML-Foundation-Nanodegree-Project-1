# Mini-Project: Movies Website

# Movie class containing information title, storyline,
# poster_image_url and trailer_youtube_url
# It contains method show_trailer to show youtube trailer of a movie

# importing modules
import webbrowser


class Movie():
    # This class provides a way to store movie related information

    VALID_RATINGS = ['A', 'B', 'C', 'D']

    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # to show trailer of a movie
        webbrowser.open(self.trailer_youtube_url)
