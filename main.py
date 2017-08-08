import webapp2
import urllib2
import urllib
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
        r_template = jinja_environment.get_template('/static/second.html')

        template_variables = {

        }
        self.response.write(r_template.render(template_variables))

app = webapp2.WSGIApplication([('/', MainHandler),('/second', SecondHandler)], debug = True)
