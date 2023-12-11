/*
Resource-01: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics

Starting:
----------
- declare variables
- semicolons at the end of a statment only required when I need to write 2 statments at the same time.
- It's best practice to write a semicolon at the end of each statment.
*/
let myVariable;

/*
- after declaring a variable I can set its value.
- JS vars has no datatype, the datatype is set by its value.
*/
myVariable = "Bob";

// I can do both at the same statment.
let myVariable2 = "Bob";

// you retrieve a variable by calling its name.
myVariable;

// Data types in JS are String, Int, Float, Bool, Arrays, Objects.
myVariable2 = [1, 'Bob', 'Steve', 10]

// Keep in mind: anything in JS is an Object and can be stores in a vraiable.

/*
Operators:
----------
- Strict Equality operator is JS is (===).
- Does-not-equal (!==)
*/

// Conditions
let iceCream = "chocolate";
if (iceCream === "chocolate") {
    alert("Yay, I have chocolate ice cream!");
} else {
    alert("Awww, but chocolate is my favourite...");
}

// Functions
let myVariable3 = document.querySelector("h1");

alert("hello!");

function multiply(num1, num2) {
    let result = num1 * num2;
    return result;
}

multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);

/*
Events:
-------
- real interactivity on a website requires handlers.
- these code structures that listen for activity in the broweser, and run code in response.
*/
// give an alert each time you click anywhere on the current html page you're in.
document.querySelector("html").addEventListener("click", function () {
    alert("Ouch! Stop poking me!")
});


document.querySelector("html").addEventListener("click", () => {
    alert("Ouch! Stop poking me!")
})

/* 
Major Example:
---------------
using JS and DOM API features to alternate the display of one or two images. this change will happen as a user clicks the displayed image.
*/
const myImage = document.querySelector("img");

myImage.onclick = () => {
    const mySrc = myImage.getAttribute("src");
    if (mySrc === "images/firefox-icon.png") {
        myImage.setAttribute("src", "images/firefox2.png")
    } else {
        myImage.setAttribute("src", "images/firefox-icon.png")
    }
};

/*
Adding a Personalized welcome message:
--------------------------------------
1. create button tag to your html page.
2. create these button and headings in JS file.
3. add function to set the personalized greeting message.
4. Add the following condition block.
5. Put this onclick event handler on the button.

- handling if the Name is Null.
*/

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    localStorage.setItem("name", myName);
    myHeading.textContent = `Mozilla is cool, ${myName}`;
}

if (!localStorage.getItem("name")) {
    setUserName();
} else {
    const storeName = localStorage.getItem("name");
    myHeading.textContent = `Mozilla is cool, ${storeName}`;
}

myButton.onclick = () => {
    setUserName();
};

// Total function
function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
        setUserName();
    } else {
        localStorage.setItem("name", myName);
        myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
};
