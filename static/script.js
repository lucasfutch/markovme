userMessages = [];

function myFacebookLogin() {
	console.log("Logging in");
	FB.login(function(){
		console.log("Logged in successfully!")
	}, {scope: 'user_posts'});
}

function myFacebookData() {
	console.log("Getting data");

	FB.api("/me/posts",
    function (response) {
      	if (response && !response.error) {
      		console.log(response);
      		for (var i = 0; i < response.data.length; i++) {
      			if (response.data[i].hasOwnProperty('message')) {
      				$("#mainText").append("<p>" + response.data[i].message + "</p>");
      				userMessages.push(response.data[i].message);
      			}
      		}

      		if (response.data.length != 0 && response.paging.next) {
      			Paginate(response.paging.next);
      		}	
     	}
    });
}

function Paginate(nextPage) {
	console.log("Paginating!");
	FB.api(nextPage,
	function(response) {
		if (response && !response.error) {
			console.log(response);

			for (var i = 0; i < response.data.length; i++) {
      			if (response.data[i].hasOwnProperty('message')) {
      				$("#mainText").append("<p>" + response.data[i].message + "</p>");
      				userMessages.push(response.data[i].message);
      			}
      		}

			userMessages.push(response);
			if (response.data.length != 0 && response.paging.next) {
				Paginate(response.paging.next);
			}
			else {
				console.log("DONE!");
				$.ajax({
				    url: "/list",
				    type: "POST",
				    data: JSON.stringify({x: userMessages}),
				    contentType: "application/json; charset=utf-8",
				    success: function(dat) { console.log(dat); },
				    error: function(e) {console.log(e);}
				});
			}
		}
	}
	)
}

$(document).ready(function(){

  $("#loginButton").click(function(){
  	  myFacebookLogin();
  });
  $("#getDataButton").click(function(){
  	  myFacebookData();
  });

});