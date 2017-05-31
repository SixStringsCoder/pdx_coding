/**
 * Created by mbp on 5/30/17.
 */
/* ************************* */
/* your javascript goes here */

// inside the function below is where you will
// do your work
// the transform function takes a string as an input
// and print out the result using the `printResult`
// function
// you can add more functions above to keep your
// code clean and readable
function transform(input) {
  if (input) {
    clearError();
    // do some transform of the user's input
    // vvvvvv HERE vvvvvv
    intify = parseInt(input, 10);
    var running_total = intify;

    var quarters = Math.floor(intify / 25);
    running_total -= quarters * 25;

    var dimes = Math.floor(running_total / 10);
    running_total -= dimes * 10;

    var nickels = Math.floor(running_total / 5);
    running_total -= nickels * 5;

    var pennies = Math.floor(running_total / 1);
    running_total -= pennies;

    // your stuff HERE
    var result = input;

    // ^^^^^^ HERE ^^^^^^
    // when you've done the transform,
    // print the result

    var message = "You get "
              + quarters + " quarters, "
              + dimes + " dimes, "
              + nickels + " nickels, "
              + pennies + " pennies back!";

    printResult(message);
  }
  else {
    printError('Enter a value');
    focusInput();
  }
}

document.addEventListener('DOMContentLoaded', function (evt) {
  // you can rename the `transform` function
  // above, but if you do, you need to change
  // the name here, too
  setup(transform);
  focusInput();
});

/* ************************************** */
/* do not change anything below this line */

function focusInput() {
  document.querySelector('[name="input"]').focus();
}

function printResult(str) {
  document.getElementById('result').innerHTML = str;
}

function printError(str) {
  var err = document.getElementById('error');
  err.classList.add('error');
  err.innerHTML = str;
}

function clearError() {
  var err = document.getElementById('error');
  err.innerHTML = '';
  err.classList.remove('error');
}

function setup(callback) {
  document.querySelector('form')
    .addEventListener('submit', function (evt) {
    evt.preventDefault();
    var value = document.querySelector('input').value;
    callback(value);
  });
}
