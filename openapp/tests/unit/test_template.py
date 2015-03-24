import openapp.api.template.template as template
import unittest
import webob


class FakeApp(object):

    def __call__(self, env, start_response):
        return Response(body = "OK")(env, start_response)

class RestTest(unittest.TestCase):
    def test_template_application(self):
        request = webob.Request.blank('/template')
        request.headers["X-Auth-Token"] = "test-token"
        response = request.get_response(template.application)
        self.assertEqual(response.body, "Sample API Test Return OK\n")
