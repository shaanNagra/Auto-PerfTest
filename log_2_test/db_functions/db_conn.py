#!/usr/bin/env python

import pymongo

from .db_constants import Database

# ////////////////FILE DESCRIPTION/////////////////
# connects to databse, returns client object that
#  can interact with collections
# /////////////////////////////////////////////////


def connect(url=Database.url, port=Database.port, database=Database.name):
    try:
        client = pymongo.MongoClient(url, port)
        return client[database]
    except pymongo.errors.PyMongoError as e:
        print("ERR: failed to connect")
        print("ERR: " + e)
