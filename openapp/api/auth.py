from webob.dec import wsgify
from webob import exc
 
@wsgify.middleware
def auth_filter(request, app):
    if request.headers.get('X-Auth-Token') == 'test-token' and \
       request.path_info == "/template":
        return app(request) 
    else:
        return exc.HTTPForbidden()
 
def filter_factory(global_config, **local_config):
    return auth_filter 
