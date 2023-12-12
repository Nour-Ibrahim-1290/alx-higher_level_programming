/* 
 * Resource: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics
 
 Objects and Classes:
 --------------------
 * Objects in JS looks like a dict.
 */

const person = {
	name: ["Bob", "Smith"],
	age: 32,
	bio: function () {
	  console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
	},
	introduceSelf: function () {
	  console.log(`Hi! I'm ${this.name[0]}.`);
	},
};

// when an object memeber is a function, it'll be written as follow
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio() {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf() {
    console.log(`Hi I'm ${this.name[0]}.`);
  },
};

// an Object property itself could be an object like 'name'
const person = {
  name: {
    first: "Bob",
    last: "Smith",
  },
  // rest of person's properties
};

// an Object could be called in both Dot and bracket notation like a Dict or a JSON
// You can create a log property function to access object's properties in a safe manner
function logProperty(propertyName) {
  console.log(person[propertyName])
}

logProperty("name");
// ["Bob", "Smith"]
logProperty("age");
// 32

// Object peroperties could be setted diff. values after its initiation.


/*
 Constructors:
 -------------
 * A way to define the shape of an Object and allow us to use it several times without reddening its shape.
 * The first version to create an object shape is just creating a function.
 */

function createPerson(name) {
  const obj = {};
  obj.name = name;
  obj.introduceSelf = function() {
    console.log(`Hi I'm ${this.name}.`);
  };
  return obj;
}

// The second way is to define a constructor
// A constructor is just a function called using the new keyword.
// Constructors by convension start with a Caital letter
function Person(name) {
  this.name = name;
  this.introduceSelf = function {
    console.log(`Hi I'm ${this.name}.`);
  };
}

// remeber the Notification API
const myNotification = new Notification("Hello!");
