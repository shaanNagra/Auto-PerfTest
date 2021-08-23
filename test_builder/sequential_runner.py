#!/usr/bin/env python

import time
import sys
from bson.objectid import ObjectId


from db_functions import db_appID
from session_clusterer import cluster_new
from session_grouper import grouping
from session_validator import validate

# ////////////////FILE DESCRIPTION/////////////////
# sequentialy runs the the testbuilder module
# does not do more advanced task manangment
# clusters groups and builds test as if pipeline
# /////////////////////////////////////////////////


def run(app):
    print("OUT: STARTING SeqRunner")
    print("                       ")
    id = db_appID.get(app)
    if id is None:
        print("OUT: STOPPED -> did not find app")
        return
    else:
        print("                      ")
        print("OUT: running clusterer")
        print("-----------------------")
        cluster_new.run(ObjectId(id))

        time.sleep(3)
        print("-----------------------")
        listOfGroups = grouping.GroupSessionsViaVersion(ObjectId(id), '1.0')
        validGroups = validate.validate(listOfGroups)
        print("DONE")


if len(sys.argv) != 2:
    print("ERR: please provide a name of application")
else:
    print(sys.argv)
    run(str(sys.argv[1]))
