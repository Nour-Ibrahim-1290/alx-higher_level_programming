/*
Resource-02: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables

Starting:
----------
- Declaring with var allowing more than one variable with the same name, while declaring with let dosen't do that.
- JS is a dynamically typed language, which means we don't specify variables datatypes, and a variable's datatype could be changed dynamically in action.


HTML code for the next JS Code:
--------------------------------
<button id="button_a">Press me</button>
<h3 id="heading_a"></h3>
*/
const buttonA = document.querySelector("#button_a");
const headingA = document.querySelector("#heading_a");

// if we don't use a var to store the name, the prompt will ask for the name each time we need to display or use it.
buttonA.onclick = () {
    const name = prompt("What is your name?");
    alert(`Hello ${name}, nice to see you!`);
    headingA.textContent = `Welcome ${name}`;
};

// declaring dict could be done straight forward this way
let dog = {name: "Spot", bread: "Dalmatian"};
dog.name;

/*
Constants:
-----------
- They're declared using const keyword.
- you must initialize them when you declare them
- you can't assign them a new value after you're initialized them.
- Using const, let's you know that this name will never be assigned to a different value.
*/

const bird = { species: "Kestrel"};
console.log(bird.species);

bird.species = "Striated Caracara";
console.log(bird.species);

