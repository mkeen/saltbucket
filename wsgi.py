#!/usr/bin/env python
# encoding: utf-8

import cherrypy

from . import app

def get_application(*args):
  opts_tuple = args

  def wsgi_app(environ, start_response):
      root, _, conf = opts_tuple or app.get_app()
      cherrypy.config.update({"environment": "embedded"})

      cherrypy.tree.mount(root, "/", conf)
      return cherrypy.tree(environ, start_response)

  return wsgi_app

application = get_application()
