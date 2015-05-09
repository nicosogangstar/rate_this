function get_popular(timeFrame, start, end){
	$.ajax({
		"method":"POST",
		"url":"popular",
		"data": {
			"time":timeFrame,
			"start":start,
			"end":end
		},

		//return handlers
		"success":function( response ){
			console.log(response);
			if(response.img.len == response.points.len){
				for(var i=0; i<response.img.len; i++){
					var item = "<img id='image' src='"+response.img[i]+"' score='"+response.points[i]+"' />";
					console.log("Item to be appended: "+item);
					$("#all").append(item);
				}
			}else{
				console.log("There was an error downloading the images")
			}
		},
		"error":function(){
			console.log("Kek u ded D:");
		}
	});
}

function get_newest(start, end){
	$.ajax({
		method:"POST",
		url:"newest",
		data: {
			"start":start,
			"end":end
		},

		//return handlers
		success:function( response ){
			console.log(response);
			if(response.img.len == response.points.len){
				for(var i=0; i<response.img.len; i++){
					var item = "<img id='image' src='"+response.img[i]+"' score='"+response.points[i]+"' />";
					console.log("Item to be appended: "+item);
					$("#all").append(item);
				}
			}else{
				console.log("There was an error downloading the images")
			}
		},
		error:function(){
			console.log("Kek u ded D:");
		}		
	});
}
