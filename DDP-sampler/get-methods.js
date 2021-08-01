Meteor.startup(() =>{
    const allMethods = Meteor.server.method_handlers
    const allPublications = Meteor.server.publish_handlers
    print(allMethods,allPublications)
});
export const name = 'get-methods';