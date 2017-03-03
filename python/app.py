import webapp2
from python import pages

app = webapp2.WSGIApplication([
    ('/', pages.MainPage),
    ('/newpost', pages.NewPost),
    ('/([0-9]+)',pages.PostPage)
], debug=True)