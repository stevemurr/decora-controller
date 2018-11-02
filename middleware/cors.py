

class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', 'GET, POST')
        resp.set_header("Access-Control-Allow-Headers",
                        "X-Custom-Header, murrkey")
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
