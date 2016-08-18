import bs4
import urllib
import re
from MovieReviewWebsite.site_generator import media

# Created by Richard Sipes 8/16/2016.
# HTML parser for automated web retrieval of Quentin Tarantino filmography.
# Parses wikipedia and youtube html files to retrieve movie title, image, and trailer urls.
# Writes movie data to file.

domain = "https://en.wikipedia.org"

# Returns movie titles and wikipedia movie page urls
def parse_tarantino_html(file):
    soup = bs4.BeautifulSoup(open(file), "html.parser")
    a_tags = soup.select("tbody a")
    links = []
    movies = []
    for a in a_tags:
        relative_path = a["href"]
        movie = a.string
        movie_url = domain + relative_path
        links.append(movie_url)
        movies.append(movie)
    return movies, links

def get_movie_poster_urls(movie_urls):
    movie_img_urls = []
    for url in movie_urls:
        # Get wikipedia movie page
        soup = bs4.BeautifulSoup(urllib.urlopen(url), "html.parser")

        # Find first img tag with a src containing .jpg or .png
        img_tags = soup.find_all("img", src=re.compile(".jpg"))
        if len(img_tags) == 0:
            img_tags = soup.find_all("img", src=re.compile((".png")))

        # Add movie image url to the list
        try:
            movie_img_url = "https://" + img_tags[0]["src"]
            movie_img_urls.append(movie_img_url)
        except IndexError:
            print("IndexError on url: " + url)

    return movie_img_urls

def get_trailer_urls(movie_titles):
    trailer_urls = []
    for title in movie_titles:
        # Query youtube
        title = title.replace(' ', '+')
        url = "https://www.youtube.com/results?search_query=" + title
        soup = bs4.BeautifulSoup(urllib.urlopen(url), "html.parser")

        # traverse DOM to get video ID
        div = soup.find("div", id=re.compile("results"))
        ol_tag = div.find("ol", class_=re.compile("item-section"))
        div = ol_tag.find("div")
        id = div["data-context-item-id"]

        # add trailer url to the list
        trailer_url = "https://www.youtube.com/watch?v=" + id
        trailer_urls.append(trailer_url)

    return trailer_urls

def get_movies(file):
    movies_titles, movie_urls = parse_tarantino_html(file)
    movie_img_urls = get_movie_poster_urls(movie_urls)
    youtube_urls = get_trailer_urls(movies_titles)
    movies = []
    for i in range(len(youtube_urls)):
        movie = media.Movie(movies_titles[i], movie_img_urls[i], youtube_urls[i])
        movies.append(movie)
    return movies

if __name__ == "__main__":
    # using simplified wikipedia html since BeautifulSoup had issues parsing full wikipedia page.
    file = "tarantino_wiki_simple.html"
    movies = get_movies(file)
    try:
        fhand = open("tarantino_films.txt", "w")
        for movie in movies:
            fhand.write(movie.info())
    except IOError:
       print(IOError)
    finally:
        fhand.close()
