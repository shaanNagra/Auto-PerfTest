import { fetch, Headers } from 'meteor/fetch';

Meteor.methods({
    'sampler.transmit'(loggedOp,timestamp,sessionID){
        //loggedOp = JSON.stringify(loggedOp);
        fetch('http://localhost:3031/operation', {
            method: 'POST',
            headers: new Headers({
                Authorization: 'Bearer my-secret-key',
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify({"temptoken":"todoapp","sessionID":sessionID,"loggedOp":loggedOp,"timestamp":timestamp})
        })
        .then(res => res.json()) // or res.json()
        .then(res => console.log(res)) 
    },

    'sampler.init'(sessionID){
        fetch('http://localhost:3031/session', {
            method: 'POST',
            headers: new Headers({
                Authorization: 'Bearer my-secret-key',
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify({"temptoken":"todoapp","sessionID":sessionID})
        })
        .then(res => res.json()) // or res.json()
        .then(res => console.log(res))
    }
});
Meteor.startup(()=>{console.log(Meteor.default_server.stream_server.all_sockets())});
export const name = 'transmit-log';