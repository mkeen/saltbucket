#from salt.runner import RunnerClient

import cherrypy

logger = logging.getLogger(__name__)

class app(object):
  @cherrypy.expose
  def index(self):
      return "Hello World!"
