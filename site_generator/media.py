import webbrowser

# Created by Richard Sipes 8/16/2016

class Movie():
    """
        A structure for displaying a video and
        storing its information.
    """
    def __init__(self, title, img_url, trailer_url):
        self.title = title
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def info(self):
        return self.title + "\n" + self.poster_image_url + "\n" + self.trailer_youtube_url + "\n"

# Unit Testing
if __name__ == '__main__':
    mulan = Movie("Mulan",
                  "https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG",
                  "https://www.youtube.com/watch?v=MsAniqGowKE")
    print(mulan.info())
    mulan.show_trailer()

