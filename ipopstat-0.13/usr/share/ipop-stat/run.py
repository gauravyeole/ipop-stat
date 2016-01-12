#!/usr/bin/env python

from flask import Flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from ipop_stats.app import create as create_app
import argparse
import os, os.path

parser = argparse.ArgumentParser(description="Standalone test server for "
                                             "ipop-stats")

try:
    default_config_path = os.path.abspath(os.environ["IPOP_STATS_SETTINGS"])
except:
    default_config_path = "config/debug.yml"

parser.add_argument(
    "-c", "--config",
    default=default_config_path,
    type=os.path.abspath,
    help="the flask config file for the server"
)

# Create Flask APP
args = parser.parse_args()
app = create_app(**vars(args)) #run(host="0.0.0.0", port=8080)

# Run with Tonado
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(8080)
IOLoop.instance().start()
