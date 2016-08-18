import media
import fresh_tomatoes

#######################################################
# Created by Richard Sipes 8/17/2016.                 #
# Generates a Quentin Tarantino filmography website   #
# by parsing tarantino_films.txt, creating a list of  #
# media.Movie objects, and passing the list to the    #
# website generator fresh_tomatoes.py                 #
#######################################################

if __name__ == "__main__":
    movies = []
    filename = "../filmography/tarantino_films.txt"
    fhand = open(filename, 'r')
    try:
        while True:
            movie_title = fhand.readline()
            movie_img_url = fhand.readline()
            trailer_youtube_url = fhand.readline()
            if not trailer_youtube_url:
                break
            movie = media.Movie(movie_title, movie_img_url, trailer_youtube_url)
            movies.append(movie)
    except IOError:
        print("IOERROR")
    finally:
        fhand.close()

    fresh_tomatoes.open_movies_page(movies)


