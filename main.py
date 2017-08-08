import webapp2
import urllib2
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello this is second page')

app = webapp2.WSGIApplication([('/', MainHandler),('/second', SecondHandler)], debug = True)
