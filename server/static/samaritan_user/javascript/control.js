$(document).ready(function() {
// put code here
})

const arrow_keys = {
	37: 'left',
	38: 'forward',
	39: 'right',
	40: 'backward'
};
const curr_down = {
	'left': false,
	'right': false,
	'forward': false,
	'backward': false
};

$(document).on('keydown', function(event) {
	const arrow_key = arrow_keys[event.keyCode];

	if (!arrow_key) {
		return;
	}

	curr_down[arrow_key] = true;
	console.log("keydown " + JSON.stringify(curr_down));
	
	$.ajax({
		url: '/send_key/',
		type: 'post',
		dataType: 'json',
		contentType: 'application/json; charset=utf-8',
		data: JSON.stringify(curr_down),
		success: function() {
			console.log(`Sent ${arrow_key} to the server`);
		},
		error: function() {
			console.log('err');
		}
	})	
});

$(document).on('keyup', function(event) {
	const arrow_key = arrow_keys[event.keyCode];

	if (!arrow_key) {
		return;
	}

	curr_down[arrow_key] = false;
	console.log("keyup " + JSON.stringify(curr_down));
})