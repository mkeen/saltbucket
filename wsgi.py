#!/usr/bin/env python
# encoding: utf-8
import cherrypy

logger = logging.getLogger(__name__)

class app(object):
  @cherrypy.expose
  def index(self):
      return "Hello World!"


def get_application(*args):
  opts_tuple = args

  def wsgi_app(environ, start_response):
    cherrypy.config.update({"environment": "embedded"})
    cherrypy.tree.mount(app, "/", {})
    return cherrypy.tree(environ, start_response)

  return wsgi_app

application = get_application()
