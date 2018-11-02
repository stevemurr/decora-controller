import logging
import falcon
from .util import get_timestring


def BasicLogger():
    """ setup_logger returns a middleware logging object for use with the falcon API """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    class ResponseLoggerMiddleware(object):
        def __init__(self, logger):
            self.logger = logger

        def process_resource(self, req, resp, resource, params):
            self.logger.info("{} {}".format(get_timestring(), resource))

        def process_response(self, req, resp, resource, req_succeeded):
            if resp.status != falcon.HTTP_200:
                return
            self.logger.info('{0} [{1} {2} {3}]'.format(
                get_timestring(),
                req.method,
                req.relative_uri,
                resp.status))

    return ResponseLoggerMiddleware(logger)
