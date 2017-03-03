from python import Handler
from python import database
from google.appengine.ext import db


class MainPage(Handler.Handler):
    def get(self):
        blog_queried = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC LIMIT 10")
        self.render("index.html", blog_queried=blog_queried)


class NewPost(Handler.Handler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get("subject")
        blog = self.request.get("blog")

        if subject and blog:
            blog_posted = database.Blog(subject=subject, blog=blog)
            blog_posted.put()
            self.redirect('/%s' % str(blog_posted.key().id()))

        else:
            error = "Come on man! You need a subject and a blog for our readers!"
            self.render("newpost.html", error=error)


class PostPage(Handler.Handler):
    def get(self, post_id):
        key = db.Key.from_path('Blog', int(post_id))
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", blog_post=post)
