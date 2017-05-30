/*
  Created by Steve Hanlon on 5/29/17.  Taking Python labs and translating them to JS
 */


// Calculate then respond
function result(name, age) {
    var next_year = age + 1;
    alert("Well, " + name + " that means you'll be " + next_year + " a year from now!");
}


// Gather info from user
function questions() {
    var name = prompt("What's your name?");
    var age = parseInt(prompt("How old are you?"));

    result(name, age);
}