/*
 *  Handles Google oauth login, and stores user information in Flask client.
*/

var clicked = false;

(function(){
	var po = document.createElement('script');
	po.type = 'text/javascript'; po.async = true;
	po.src = 'https://apis.google.com/js/client:plusone.js?onload=render';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(po, s);
})();

function render() {
	gapi.signin.render('customBtn', {
		'callback': 'signinCallback',
		"clientid" : "254876227003-am9vcg2ja4inntpocgarioptqift33ur.apps.googleusercontent.com",
		'cookiepolicy': 'single_host_origin',
		'scope': 'profile'
	});
}

$("#customBtn").click(function() {
 	clicked = true;
});

function signinCallback(authResult) {
	if (authResult['status']['signed_in']) {
		console.log("login suceeed");
		gapi.client.load('plus','v1', function(){
			var request = gapi.client.plus.people.get({'userId': 'me'});
			request.execute(function(resp) {
				console.log(resp);
				// store person object in Flask session
				$.ajax({
					type : "POST",
					url : "/googleoauth",
					data : JSON.stringify(resp, null, '\t'),
					contentType : "application/json;charset=UTF-8",
				})
			});
		});
		if (clicked) {
			location.reload();
			clicked = false;
		}
		
	}
	else {
		// Update the app to reflect a signed out user
		// Possible error values:
		//	 "user_signed_out" - User is signed-out
		//	 "access_denied" - User denied access to your app
		//	 "immediate_failed" - Could not automatically log in the user

		console.log('Sign-in state: ' + authResult['error']);
	}
}
