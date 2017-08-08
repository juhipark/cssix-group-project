import webapp2
import urllib2
import urllib
import json
import jinja2
import os

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class SecondHandler(webapp2.RequestHandler):
    def get(self):
        r_template = jinja_environment.get_template('/static/second.html')

        template_variables = {

        }
        self.response.write(r_template.render(template_variables))

app = webapp2.WSGIApplication([('/', MainHandler),('/second', SecondHandler)], debug = True)
