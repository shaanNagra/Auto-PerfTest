#!/usr/bin/env python

# ////////////////FILE DESCRIPTION/////////////////
# hardcoded constants that are used for database
# NOTE: used during rapid prototyping
# /////////////////////////////////////////////////

class AppCol:
    name = 'applications'
    token = 'token'
    version = '1.0'
    id = '_id'


class SessionCol:
    name = 'sessions'
    application = 'webapp'
    processed = 'processed'
    id = '_id'
    loggedId = 'user_session_id'
    appVersion = 'app_version'


class CallCol:
    name = 'calls'
    session = 'session_id'
    id = '_id'
    operation = 'operation'
    message = 'message'
    time = 'time'
    label = 'label'


class Database:
    url = 'localhost'
    port = 27017
    name = 'K-Base'
