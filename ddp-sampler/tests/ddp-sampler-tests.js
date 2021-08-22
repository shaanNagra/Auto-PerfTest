// Import Tinytest from the tinytest Meteor package.
import { Tinytest } from "meteor/tinytest";

// Import and rename a variable exported by ddp-sampler.js.
import { name as packageName } from "meteor/ddp-sampler";

// Write your tests here!
// Here is an example.
Tinytest.add('ddp-sampler - example', function (test) {
  test.equal(packageName, "ddp-sampler");
});
