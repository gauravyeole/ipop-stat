from ..errors import *
from flask import Blueprint, request, jsonify
from flask import current_app as app
import datetime
import socket
import uuid
import logging

from pymongo import MongoClient


submit = Blueprint("submit", __name__, url_prefix="/api")

@submit.route("/submit", methods=["POST"])
def update():
    logger = logging.getLogger('all')
    logger.info("Report Message Received")
    data = request.json
    report = {"Report": data}
    obj_id = app.database.user_collection.insert_one(report)
    response = jsonify(result=uuid.uuid4().hex, status="success") # TODO: what is result?
    return response

@submit.route("/")
def hello():
    return "IPOP-Usage Stat Server!"

@submit.route("/generate_uuid")
def generate_uuid():
    """Convenience uuid generator, for clients who don't have a convenient local
    generator."""
    response = jsonify(result=uuid.uuid4().hex, status="success")
    response.headers["Expires"] = "-1"
    response.headers["Cache-Control"] = "no-cache, no-store"
    return response
