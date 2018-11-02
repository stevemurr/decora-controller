import argparse
import falcon
import json
import io
import os
import middleware
import waitress
import hooks
import resource
import decora


def setup_args():
    args = argparse.ArgumentParser()
    args.add_argument("--email", default="")
    args.add_argument("--password", default="")
    args.add_argument("--port", help="Port to host on.", default=8888)
    args.add_argument(
        "--webdriver", help="Path to webdriver.  If empty then try a chromedriver on the $PATH.")
    return args.parse_args()


if __name__ == "__main__":
    args = setup_args()
    api = falcon.API(
        middleware=[middleware.HandleCORS(), middleware.BasicLogger(), middleware.ErrorLogger()])

    d = decora.Decora(args.email, args.password)
    print(d.get_switches())
    decora_resource = resource.DecoraResource(d)

    api.add_route("/api/{device_id}", decora_resource)
    api.add_route("/api/{device_id}/{param}", decora_resource)
    api.add_route("/api/{device_id}/{param}/{value}", decora_resource)

    waitress.serve(api, host="0.0.0.0", port=args.port)
