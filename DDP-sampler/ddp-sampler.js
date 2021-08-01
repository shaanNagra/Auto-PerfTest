// Write your package code here!

// log sent messages
var _send = Meteor.connection._send;
Meteor.connection._send = function (obj) {
console.log("send", obj);
_send.call(this, obj);
};

// log received messages
Meteor.connection._stream.on('message', function (message) { 
console.log("receive", JSON.parse(message)); 
});

// Variables exported by this module can be imported by other packages and
// applications. See ddp-sampler-tests.js for an example of importing.
export const name = 'ddp-sampler';
