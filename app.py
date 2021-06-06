#from salt.runner import RunnerClient

import cherrypy

logger = logging.getLogger(__name__)

class SaltBucketApp(object):
  @cherrypy.expose
  def index(self):
      return "Hello World!"

def get_app(opts):
    apiopts = opts.get(__name__.rsplit(".", 2)[-2], {})

    root = SaltBucketApp()
    cpyopts = root.get_conf()

    return root, apiopts, cpyopts
