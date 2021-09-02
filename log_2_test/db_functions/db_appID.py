#!/usr/bin/env python

import pymongo

from db_functions.db_constants import AppCol
from db_functions import db_conn
# ////////////////FILE DESCRIPTION/////////////////
# connects to databse, returns object id of webapp
# /////////////////////////////////////////////////


def get(name):
    client = db_conn.connect()
    try:
        result = client.applications.find_one({AppCol.name: name})
        if result is None:
            return None
        print("OUT: application (" + str(result[AppCol.name]) + ") found")
        return result[AppCol.id]
    except pymongo.errors.PyMongoError as e:
        print(e)
