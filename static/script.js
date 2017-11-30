
/////////////////////////////////////////////////////////////////////
//// FB LOGIN FLOW //////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////

window.fbAsyncInit = function() {
FB.init({
  appId            : 2000850609943113,
  autoLogAppEvents : true,
  xfbml            : true,
  version          : 'v2.11'
});
};

(function(d, s, id){
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) {return;}
		js = d.createElement(s); js.id = id;
		js.src = "https://connect.facebook.net/en_US/sdk.js";
		fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////

userMessages = [];

function myFacebookLogin() {
	console.log("Logging in");
	FB.login(function(response){
		if (response.authResponse) {
     		var access_token =   FB.getAuthResponse()['accessToken'];
			console.log("Logged in successfully!")
			$("#getDataFBButton").show();
		$("#mainText").append("<p>You have successfully logged in!</p>");
	}}, {scope: 'user_posts'});
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
      		if (response.data.length < 1 ){
      			$("#mainText").append("<p>Sorry, we were not able to get permission to get access to your facebook posts. Facebook is still reiewing our app.</p>");
			}
      		for (var i = 0; i < response.data.length; i++) {
      			if (response.data[i].hasOwnProperty('message')) {
      				//$("#mainText").append("<p>" + response.data[i].message + "</p>");
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
      				//$("#mainText").append("<p>" + response.data[i].message + "</p>");
      				userMessages.push(response.data[i].message);
      			}
      		}

			if (response.data.length != 0 && response.paging.next) {
				Paginate(response.paging.next);
			}
			else {
				console.log("DONE!");
				$("#loading").html("");
				$("#loaderThing").hide();
				$.ajax({
				    url: "/list",
				    type: "POST",
				    data: JSON.stringify({x: userMessages}),
				    contentType: "application/json; charset=utf-8",
				    success: function(data) { $("#mainText").append("<p>" + data.result + "</p>"); },
				    error: function(e) {console.log(e);}
				});
			}
		}
	}
	)
}

$(document).ready(function(){
	$("#getDataFBButton").hide();

	$("#loginFBButton").click(function(){		
  		$("#mainText").html("");
  		myFacebookLogin();
	});

	$("#getDataFBButton").click(function(){
  		$("#mainText").html("");
		$("#middle").append('<div id = "loaderThing" class="loader"></div>');
  		myFacebookData();
	});

	$("#getDataInputButton").click(function(){
		$("#getDataFBButton").hide();
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
		$("#getDataFBButton").hide();
		$("#mainText").html("Coming soon!");
	});

});