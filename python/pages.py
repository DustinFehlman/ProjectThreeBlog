from python import Handler
from python import database
from google.appengine.ext import db


class MainPage(Handler.Handler):
    def get(self):
        self.render("index.html")


class PostPage(Handler.Handler):
    def get(self):
        self.render("post.html")

    def post(self):
        subject = self.request.get("subject")
        blog = self.request.get("blog")

        if subject and blog:
            blog_posted = database.Blog(subject=subject, blog=blog)
            blog_posted.put()
            blog_queried = db.GqlQuery("SELECT * FROM Blog ORDER BY created DESC")
            for x in blog_queried:
                self.write(x.subject)
                self.write(x.created)
        else:
            self.write("Nope!")
