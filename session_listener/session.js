module.exports.init = function (db,data){
    db.collection("applications").findOne({token:data.token},function(err,result){
        if(result){
            var id = ""+data.token+data.sessionID;
            var doc = {
                _id:id,
                webapp:result._id,
                processed:false,
                user_session_id:data.sessionID,
                app_version:result.curr_version
            };
            db.collection("sessions").insertOne(doc,function(err,res){
                if(err) return false;
                return true
            });
        }
    });
    return false;
};

module.exports.saveOp = function (db,data){

    var id = ""+data.token+data.sessionID;
    if(data.loggedOp.msg== 'sub' || data.loggedOp.msg== 'usub'){
        var operation = data.loggedOp.msg+" "+data.loggedOp.name
    }
    else if(data.loggedOp.msg == 'method'){
        var operation = data.loggedOp.msg+" "+data.loggedOp.method
    }
    else{
        return false
    }

    var doc = {
        session_id:id,
        time:data.timestamp,
        operation:operation,
        message:data.loggedOp,
    };

    db.collection("calls").insertOne(doc,function(err,res){
        if(err) return false;
        return true
    });
};

