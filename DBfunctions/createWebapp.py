#!/usr/bin/python

import pymongo

def connect(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        print("could not connect to database")
        return None


def init(name,token,base_version):
    client = connect()
    try:
        doc = {'name':name,'token':token,"curr_version":base_version}
        x = client.applications.insert_one(doc)
        print(x.inserted_id)
    except:
        pass