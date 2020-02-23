$(document).ready(function() {
// put code here
})

const arrow_keys = {
	37: 'left',
	38: 'up',
	39: 'right',
	40: 'down'
};

$(document).on('keydown', function(event) {
	const arrow_key = arrow_keys[event.keyCode];

	if (!arrow_key) {
		return;
	}

	$.ajax({
		url: '/send_key/',
		type: 'post',
		dataType: 'json',
		contentType: 'application/json; charset=utf-8',
		data: JSON.stringify({'key': arrow_key}),
		success: function() {
			console.log(`Sent ${arrow_key} to the server`);
		},
		error: function() {
			console.log('um');
		}
	})	
})