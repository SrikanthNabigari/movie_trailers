import webbrowser

class Movie():
    """This is the Movie class where movie instances are been inserted"""
    def __init__(self,movie_title,movie_storyline,poster_image,trailer):
        self.title = movie_title #title of the movie
        self.storyline = movie_storyline #storyline of the movie
        self.poster_image_url = poster_image #poster image of the movie
        self.trailer_youtube_url = trailer #trailer youtube url
    def show_trailer(self):
        """ This function opens trailer youtube url when it is called"""
        webbrowser.open(self.trailer_youtube_url)
