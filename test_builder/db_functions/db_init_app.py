#!/usr/bin/env python

import pymongo

from db_functions import db_conn

# ////////////////FILE DESCRIPTION/////////////////
# create application document in collection
# /////////////////////////////////////////////////


def create(name, token, init_version):
    client = db_conn.connect()
    try:
        doc = {'name': name, 'token': token, "curr_version": init_version}
        x = client.applications.insert_one(doc)
        print('OUT: application added')
        print('OUT: ' + str(x.inserted_id))
    except pymongo.errors.PyMongoError as e:
        print("ERR: failed while creating application")
        print("ERR: "+e)
