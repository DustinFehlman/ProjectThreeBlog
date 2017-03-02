import webapp2
from python import pages

app = webapp2.WSGIApplication([
    ('/', pages.MainPage),
    ('/post', pages.PostPage),
], debug=True)