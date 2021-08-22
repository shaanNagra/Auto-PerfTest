#!/usr/bin/env python

import pymongo

from db_functions.db_constants import AppCol, Database

# ////////////////FILE DESCRIPTION/////////////////
# initial Database (Knowledge Base) if it does not exist
# NOTE: used during prototyping
# /////////////////////////////////////////////////


def run():
    try:
        client = pymongo.MongoClient(Database.url, Database.port)
        dblist = client.list_database_names()
        if Database.name in dblist:
            print("OUT: Database has already been initialized")
        else:
            db = client[Database.name]
            initCol = db[AppCol.name]
            initData = {
                AppCol.name: 'initApp',
                AppCol.token: 'notToken'
                }
            initCol.insert_one(initData)
            print("OUT: Database initialized")

    except Exception as e:
        print('ERR: failed to initialize ')
        print('ERR: '+e)
