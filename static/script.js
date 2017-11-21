userMessages = [];

function myFacebookLogin() {
	console.log("Logging in");
	FB.login(function(){
		console.log("Logged in successfully!")
		$("#mainText").append("<p>You have successfully logged in!</p>");
	}, {scope: 'user_posts'});
}

function myFacebookData() {
	console.log("Getting data");

	FB.api("/me/posts",
    function (response) {
    	if (response.error) {
    		$("#mainText").append("<p>Please login first.</p>");
    		$("#loading").html("");
    	}
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

			if (response.data.length != 0 && response.paging.next) {
				Paginate(response.paging.next);
			}
			else {
				console.log("DONE!");
				$("#loading").html("");
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

	$("#loginFBButton").click(function(){
  		$("#mainText").html("");
  		$("#loading").html("");
  		myFacebookLogin();
	});

	$("#getDataFBButton").click(function(){
  		$("#mainText").html("");
  		$("#loading").html("");
  		$("#mainText").append("<p id = 'loading'>LOADING POSTS...<br></p>");
  		myFacebookData();
	});

	$("#getDataInputButton").click(function(){
		$("#mainText").html("");
  		$("#loading").html("");
  		$.ajax({
		    url: "/upload",
		    type: "GET",
		    // data: JSON.stringify({x: userMessages}),
		    // contentType: "application/json; charset=utf-8",
		    success: function(dat) { $("#mainText").html(dat) },
		    error: function(e) {console.log(e);}
		});
	});

	$("#getDataMessengerButton").click(function(){
		$("#mainText").html("");
  		$("#loading").html("");
	});

});