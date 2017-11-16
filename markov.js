userMessages = []

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
      		userMessages.push(response);

      		if (response.paging.next) {
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
			userMessages.push(response);
			if (response.paging.next) {
				Paginate(response.paging.next);
			}
		}
	}
	)
}