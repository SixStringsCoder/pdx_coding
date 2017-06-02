/*
 Created by Steve Hanlon on June 1, 2017.
*/


function colorPicker() {
    // generate random numbers for RGB values
    let $red = Math.floor((Math.random() * 255) + 1);
    let $green = Math.floor((Math.random() * 255) + 1);
    let $blue = Math.floor((Math.random() * 255) + 1);
    // make object of $RGB values
    return {
        'red': $red,
        'green': $green,
        'blue': $blue
    };
}


function colorEffect() {
    $('.square').mouseover(
        function (event) {
            let hue = colorPicker();
            // Using tick notation use color placeholders to make random colors in square DIVs
            $(this, '#marquee').css('background-color', `rgb(${hue.red}, ${hue.green}, ${hue.blue}`).css('transition', '.6s');
            // Replace Heading <span> text with word populating DIV
            let $currentText = $(this).text();
            $('#marquee').text($currentText).css('color', `rgb(${hue.red}, ${hue.green}, ${hue.blue}`).css('transition', '.6s');
        });
}


colorEffect();