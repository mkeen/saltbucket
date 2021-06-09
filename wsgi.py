#!/usr/bin/env python
# encoding: utf-8
import cherrypy

import saltbucket

def get_application(*args):
  opts_tuple = args

  def wsgi_app(environ, start_response):
      cherrypy.config.update({"environment": "embedded"})
      cherrypy.tree.mount(saltbucket, "/", {})
      return cherrypy.tree(environ, start_response)

  return wsgi_app

application = get_application()
