import inspect
import math
import time
from xml.dom import minidom
from xml.parsers import expat

from lxml import etree
from oslo_log import log as logging
from oslo_serialization import jsonutils
from oslo_utils import excutils
import six
import webob

from openapp import exception
from openapp import i18n
from openapp.i18n import _, _LE, _LI
from openapp import utils
from openapp import wsgi
from keystoneclient.v2_0 import client

class Request(webob.Request):
    """Add some OpenStack API-specific logic to the base webob.Request."""

    def __init__(self, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)
        self._resource_cache = {}



    def get_db_snapshots(self):
        return self.get_db_items('snapshots')


    def get_keystone(data):
        username = data['username']
        password = data['password']
        if 'auth_url' in data:
            auth_url = data['auth_url']
        else:
            auth_url = "http://127.0.0.1:35357/v2.0/"

        if 'tenant_name' in data:
            tenant_name = data['tenant_name']
        else:
            tenant_name = "admin"
        try:
            return client.Client(username=username, password=password,
                tenant_name=tenant_name, auth_url=auth_url)
        except Exception:
            return "keystone login error"


    def tenant_list(json):
        keystone = get_keystone(json)
        return keystone.tenants.list()
