from webob import Response
from webob.dec import wsgify

@wsgify
def application(request):
    return Response('Sample API Test Return OK\n')
 
def app_factory(global_config, **local_config):
    return application 
