/*
  Created by Steve Hanlon on 5/30/17.
 */

/*
Write a JavaScript program to decrypt an ROT13 Encoded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
*/


var message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg.";

var encoded = message.toLowerCase();
var alphabet = "abcdefghijklmnopqrstuvwxyz, '-.";
var cesar13 =  "nopqrstuvwxyzabcdefghijklm, '-.";

var decoded = [];

function cipher(msg) {
    for (var i = 0; i < encoded.length; i += 1) {
        var enchar = encoded[i];
        var encloc = cesar13.indexOf(enchar);
        var decodedChar = alphabet[encloc];
        decoded.push(decodedChar);
    }
    var result = decoded.join('');
    document.write(result);
}


cipher(message);