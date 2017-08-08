import webapp2
import urllib2
import json
import jinja2
import os
import logging

first_string = 'Happy'
second_string = 'Sad'
jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('project.html')
        self.response.write(template.render())


class SecondHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello this is second page')

app = webapp2.WSGIApplication([('/', MainHandler),('/second', SecondHandler)], debug = True)
