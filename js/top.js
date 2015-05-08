function get_popular(timeFrame, start, end){
	$.ajax({
		"method":"POST",
		"url":"",
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

function get_newest(timeFrame, start, end){
	$.ajax({
		method:"POST",
		url:"",
		data: {
			"time":timeFrame,
		},

		//return handlers
		success:function(){
			
		},
		error:function(){
			
		}		
	});
}
