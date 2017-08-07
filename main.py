import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([('/', MainHandler)], debug = True)
