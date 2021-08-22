#!/usr/bin/env python

import pymongo

from db_functions import db_conn
from db_functions.db_constants import AppCol
# ////////////////FILE DESCRIPTION/////////////////
# create application document in collection
# /////////////////////////////////////////////////


def create(name, token, init_version):
    client = db_conn.connect()
    try:
        doc = {
            AppCol.name: name,
            AppCol.token: token,
            AppCol.version: init_version
            }
        x = client.applications.insert_one(doc)
        print('OUT: application added')
        print('OUT: ' + str(x.inserted_id))
    except pymongo.errors.PyMongoError as e:
        print("ERR: failed while creating application")
        print("ERR: "+e)
