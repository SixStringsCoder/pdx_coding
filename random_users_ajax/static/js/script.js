/*
 Created by Steve Hanlon on June 2, 2017.

 Use Ajax request to gather JSON.  Filter it and then pretty display it in browser.
*/


function showData(people) {
    "use strict";

    // Remove any present people/ID cards on web page
    $('#idCardContainer').empty();

     $('button').on('dblclick', function() {
     // Display 6 new people with image and details
     $('#idCardContainer').append(`<div class="idCard"><p><img class="idPic" src="${people.picture}"></p>
                    <p class="details"><span>Name:</span> ${people.name}</p>
                    <p class="details"><span>Email:</span> ${people.email}</p>
                    <p class="details"><span>User name:</span> ${people.username}</p>
                    <p class="details"><span>Registration date:</span> ${people.registration_date}</p>
                    <p class="details"><span>Date of birth:</span> ${people.birth_date}</p>
                    </div>`);
                    event.preventDefault();
     });

}


function parseData(dataForParsing) {
    "use strict";

    let $pattern = /\s\d{2}:\d{2}:\d{2}/;  // Regex to remove time stamp

    // Filter data from Ajax request
    $.each(dataForParsing.results, function(i, user){
        let name = user.name.first.toUpperCase() + ' ' + user.name.last.toUpperCase();
        let email = user.email;
        let userName = user.login.username;
        let regDate = user.registered.replace($pattern, '' );
        let dob = user.dob.replace($pattern, '' );
        let pic = user.picture.large;

        // Organize data in Object
        let idData = {
        name: name,
        email: email,
        username: userName,
        registration_date: regDate,
        birth_date: dob,
        picture: pic
        };

        showData(idData);
    });
}


function collectData() {
    // Ajax request from URL return JSON
    $.ajax({
        url: 'https://api.randomuser.me/',
        method: 'GET',
        data: {'results': 6},
        success: function (response) {
            console.log(response);
            // Call function to filter JSON
            parseData(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

collectData();