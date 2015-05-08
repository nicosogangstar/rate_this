function get_popular(timeFrame, start, end){
	$.ajax({
		"method":"POST",
		"url":"popular.py",
		"data": {
			"time":timeFrame,
			"start":start,
			"end":end
		},

		//return handlers
		"success":function( response ){
			console.log(response);
		},
		"error":function(){
			console.log("Kek u ded D:");
		}		
	});
}

function get_newest(start, end){
	$.ajax({
		method:"POST",
		url:"newest.py",
		data: {
			"start":start,
			"end":end
		},

		//return handlers
		success:function( response ){
			console.log(response);
		},
		error:function(){
			console.log("Kek u ded D:");
		}		
	});
}
