var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, client) {
    if (err) throw err;
    global.db = client.db("K-Base");
    //return db; if webapps have own databases
});     
