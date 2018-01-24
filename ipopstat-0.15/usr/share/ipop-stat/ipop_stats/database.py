
import logging
import uuid
import functools
from contextlib import contextmanager

from pymongo import MongoClient

class Database(object):
    def __init__(self, app):
        self.app = app

        self.stat_mongo = MongoClient(self.app.config["database_uri"])
        logger = logging.getLogger('all')
        logger.info("MongoDB Server is running at :{0}".format(self.app.config["database_uri"]))
        self._db = self.stat_mongo[self.app.config["database_name"]]
        self.user_collection = self._db["user"]

