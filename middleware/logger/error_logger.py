import logging
import falcon
from .util import get_timestring


def ErrorLogger():
    """ setup_logger returns a middleware logging object for use with the falcon API """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    class ResponseLoggerMiddleware(object):
        def __init__(self, logger):
            self.logger = logger

        def process_response(self, req, resp, resource, req_succeeded):
            if resp.status == falcon.HTTP_200:
                return

            self.logger.info("[{}] {} {}".format(
                get_timestring(), resp.status, resp.body))

    return ResponseLoggerMiddleware(logger)
