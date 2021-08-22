const express = require('express');
require('./open.js');
const session = require('./session.js');
const app = express();
const port = 3031;

app.use(express.json());


app.post('/session', (req, res) => {
  var result = session.init(db,req.body);
  return res.send(JSON.stringify("session initialized"));
});



app.post('/operation', (req, res) => {
  var result = session.saveOp(db,req.body)
  return res.send(JSON.stringify("function call logged"));
});


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
