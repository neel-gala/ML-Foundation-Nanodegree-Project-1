# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py.
# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# importing modules
import media
import fresh_tomatoes

m_3idiots = media.Movie("3 Idiots",
                        "Movie depicting modern age problem of students",
                        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=xvszmNXdM4w")

bajirao_mastani = media.Movie("Bajirao Mastani",
                              "Movie describing life of Bajirao. ",
                              "https://upload.wikimedia.org/wikipedia/en/5/52/Bajirao_Mastani_Poster_2.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=eHOc-4D7MjY")

spiderman_homecoming = media.Movie("Spiderman Homecoming",
                                   "Superhero movie about the story "
                                   "of spiderman. ",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=U0D3AOldjMU")  # NOQA

batman = media.Movie("Batman",
                     "Batman is a fictional superhero who appears in American "
                     "comic books published by DC Comics. "
                     "The character is also referred to by such "
                     "epithets as the Caped Crusader, the Dark Knight, "
                     "and the World's Greatest Detective.",
                     "https://upload.wikimedia.org/wikipedia/en/7/74/Batman_Detective_Comics_Vol_2_1.png",  # NOQA
                     "https://www.youtube.com/watch?v=PIGCKbrCVc4")

bahubali = media.Movie("Bahubali",
                       "The Beginning is a tale of the lost rightful heir "
                       " of the fictional kingdom of Mahishmati, who learns "
                       "about his true identity while falling in love with "
                       "a rebellious warrior, who (among with her group) "
                       "intends to rescue the former queen of Mahismati.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=RIOPLQkRjVk")

iron_man = media.Movie("Iron Man",
                       "Iron Man is a 2008 American superhero film based on "
                       "the Marvel Comics character of the same name. ",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",  # NOQA
                       "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

movies = [m_3idiots,
          bajirao_mastani,
          spiderman_homecoming,
          batman,
          bahubali,
          iron_man]

# creating html page showing movies info
fresh_tomatoes.open_movies_page(movies)
