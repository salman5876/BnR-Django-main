import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        print "Amad";
        print "testing"


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)