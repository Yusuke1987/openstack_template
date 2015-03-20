from oslo_log import log as logging
from webob.dec import wsgify
from webob import exc

LOG = logging.getLogger(__name__)
 
@wsgify.middleware
def auth_filter(request, app):
    if request.headers.get('X-Auth-Token') == 'test-token' and \
       request.path_info == "/template":
        return app(request) 
    else:
        LOG.debug("Template request faild")
        return exc.HTTPForbidden()
 
def filter_factory(global_config, **local_config):
    return auth_filter 
