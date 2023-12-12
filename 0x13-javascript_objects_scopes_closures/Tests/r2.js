/*
 * Resource: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
 
 Classes:
 --------
 * you can declare a class using the class keyword
 */

class Person {
  // declaring the name is optional, I could omitt it and the decleration in constructor would sufice.
  name;

  // the contructor is defined using the constructor keyword.
  constructor(name) {
    this.name = name;
  }

  introduceSelf() {
    console.log(`Hi I'm ${this.name}`);
  }
}

// creating a new object of Person class.
const giles = new Person("giles");
giles.introduceSelf(); // Hi I'm giles



// If you don't need to do any special initializations, you can omit the constructor like that
class Animal {
  sleep() {
    console.log("zzzzzz");
  }
}

const spot = new Animal();
spot.sleep(); // 'zzzzzz'


/*
 Inheritance:
 -------------
 * defining childs of parents
 */
class Professor extends Person {
  teaches;

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(
      `My Name is ${this.name}, and I will be your ${this.teaches} professor.`,
    );
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5-1) + 1);
    console.log(grade);
  }
}

/*
 Encapsulation:
 ---------------
 * making properties private to a class or a subclass.
 */
class Student extends Person {
  #year; // now year is limited to Student (private), couldn't be access from a Student object
	
  constructor(name, year) {
    super(name);
	  this.#year = year;
  }

  introduceSelf() {
    console.log(`Hi, I'm ${this.name}, and I'm in yesr ${this.#year}.`);
  }

  canStudentArchery() {
    return this.#year > 1;
  }
}

// The same goes for Private Methods
class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log("You called me!");
  }
}


const myExample = new Example();

myExample.somePublicMethod(); // 'You called me!'

myExample.#myPrivateMethod(); // SyntaxError
