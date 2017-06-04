/*
 Created by Steve Hanlon on June 2, 2017.
*/



function showData(people) {
    "use strict";
    let $pattern = /\s\d{2}:\d{2}:\d{2}/;  // use Regex to remove time stamp
         $('button').on('dblclick', function() {
         $('#idCardContainer').append(`<div class="idCard"><p><img class="idPic" src="${people.picture}"></p>
                        <p class="details"><span>Name:</span> ${people.name}</p>
                        <p class="details"><span>Email:</span> ${people.email}</p>
                        <p class="details"><span>User name:</span> ${people.username}</p>
                        <p class="details"><span>Registration date:</span> ${people.registration_date.replace($pattern, '' )}</p>
                        <p class="details"><span>Date of birth:</span> ${people.birth_date.replace($pattern, '' )}</p>
                        </div>`);
            });
}


function parseData(dataForParsing) {
    "use strict";

    $.each(dataForParsing.results, function(i, user){
        let name = user.name.first.toUpperCase() + ' ' + user.name.last.toUpperCase();
        let email = user.email;
        let userName = user.login.username;
        let regDate = user.registered;
        let dob = user.dob;
        let pic = user.picture.large;

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
    $.ajax({
        url: 'https://api.randomuser.me/',
        method: 'GET',
        data: {'results': 5},
        success: function (response) {
            console.log(response);
            parseData(response);
        },
        error: function (error) {
            console.log(error);
        }
    });


}

collectData();