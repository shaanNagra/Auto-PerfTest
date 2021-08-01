// Write your package code here!

const samplerMethods = ['sampler.transmit','sampler.init']

Meteor.startup(() =>{
    if(Math.random() < 2){

        var rand = Math.floor(Math.random() * 10000)+1000
        const sessionId = ""+rand+"_"+Date.now();
        
        Meteor.call('sampler.init',sessionId);

        
        initLogger(sessionId);

    }
});

function initLogger (sessionId){
    var _send = Meteor.connection._send;
    Meteor.connection._send = function (obj){

        if(samplerMethods.includes(obj.method) == false){
            if(obj.msg == "sub" || obj.msg == "method"){
                    
  
        
                Meteor.call('sampler.transmit', obj, Date.now(), sessionId, (error, result) => { });
            }
        }
        console.log("send", obj);
        console.log("time",Date.now()); 

        _send.call(this, obj);
    };
}

// log sent messages

// log received messages
// Meteor.connection._stream.on('message', function (message) { 
// console.log("receive", JSON.parse(message)); 
// });

// Variables exported by this module can be imported by other packages and
// applications. See ddp-sampler-tests.js for an example of importing.
export const name = 'log-ddp';
