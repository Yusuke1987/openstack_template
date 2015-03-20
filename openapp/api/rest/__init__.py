from oslo_config import cfg
from oslo_log import log as logging

from openapp.i18n import _LW


CONF = cfg.CONF
LOG = logging.getLogger(__name__)


def rest_app_factory(loader, global_conf, **local_conf):
    pass
