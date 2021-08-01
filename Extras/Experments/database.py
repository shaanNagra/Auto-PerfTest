import pymongo

def getConnection(url='localhost',port=27017,database='mydb'):
    try:
        client = pymongo.MongoClient(url,port)
        return client[database]
    except:
        return None