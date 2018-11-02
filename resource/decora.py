import falcon


class DecoraResource:
    def __init__(self, d):
        self.d = d

    def __repr__(self):
        return "DecoraResource"

    def on_get(self, req, resp, device_id, param):

        switch = self.d.switches[device_id]

        try:
            state = switch.__dict__['data'][param]
        except KeyError:
            resp.status = falcon.HTTP_400
            return
        resp.media = {param: state}
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp, device_id, param, value):

        self.d.set_param(device_id, param, value)
        resp.status = falcon.HTTP_200
