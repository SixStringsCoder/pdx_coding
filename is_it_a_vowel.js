/*
 Created by Steve Hanlon on 5/30/17.
 c
 */


function vowel() {
    var vowels = ['a','e', 'i', 'o', 'u'];
    var input = prompt("Please enter a single letter.")

    if (vowels.indexOf(input) != -1) {
        alert('The character you entered is a vowel!');
    } else {
        alert('The character you entered is a consonant!');
  }
}


vowel();