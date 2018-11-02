import falcon
import json


def validate_json(req, resp, resource, params):
    if req.content_length in (None, 0):
        return
    body = req.stream.read()
    if not body:
        raise falcon.HTTPBadRequest('Empty request body',
                                    'A valid JSON document is required.')
    try:
        req.body = json.loads(body.decode('utf-8'))
    except (ValueError, json.JSONDecodeError):
        raise falcon.HTTPError(falcon.HTTP_753,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect or not encoded as '
                               'UTF-8.')
