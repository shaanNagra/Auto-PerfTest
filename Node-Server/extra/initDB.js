const MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb";


MongoClient.connect(url, function(err, db) {
    if (err) throw err;
    var dbo = db.db("mydb");
    dbo.createCollection("webapps", function(err, res) {
        if (err) throw err;
        console.log("Webapps collection created!");
        db.close();
      });
    dbo.createCollection("sessions", function(err, res) {
      if (err) throw err;
      console.log("Sessions collection created!");
      db.close();
    });
    dbo.createCollection("sessionOps", function(err, res) {
        if (err) throw err;
        console.log("SessionOps collection created!");
        db.close();
      });
});