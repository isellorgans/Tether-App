$(document).ready(function(){
	// Loads the Dota-2 theme
	$("#dota-2-theme").on("click", function(){
		$("#intro-img-1").attr("src", 'tether/static/images/dota_1.jpg');
		$("#intro-img-2").attr("src", 'tether/static/images/dota_2');
		$("#intro-img-3").attr("src", 'tether/static/images/dota_3');
	});

	// Loads the CS:GO theme
	$("#cs-go-theme").on("click", function(){
		$("#intro-img-1").attr("src",STATIC_URL+'/images/cs-go-1');
		$("#intro-img-2").attr("src",STATIC_URL+'/images/cs-go-2');
		$("#intro-img-3").attr('src',STATIC_URL+'/images/cs-go-3.jpg');
	});

});