import openapp.api.auth as template
import unittest
import webob


class RestTest(unittest.TestCase):
    def test_auth_filter(self):
        request = webob.Request.blank('/template')
        request.headers["X-Auth-Token"] = "test-token"
        response = request.get_response(template.filter_factory)
#        self.assertEqual(expected, actual)
#if __name__ == "__main__":
#    unittest.main()
