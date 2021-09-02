#!/usr/bin/env python

import pymongo

from db_functions import db_conn
from db_functions.db_constants import SessionCol, CallCol

# ////////////////FILE DESCRIPTION/////////////////
# functions that interact with the mongodb database
#  for use in the grouping functionallity
#  (is the interface for grouping module)
# /////////////////////////////////////////////////


# class Database:
#     url = 'localhost'
#     port = 27017
#     name = 'K-Base'


# class CallCol:
#     name = 'calls'
#     session = 'session_id'
#     id = '_id'
#     operation = 'operation'
#     message = 'message'
#     time = 'time'
#     label = 'label'