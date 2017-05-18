
	// Open and Close Options Panel
	$( "#options-panel .panel-button" ).click(function(){
		$( "#options-panel" ).toggleClass( "close-panel", "open-panel", 800 );
		$( "#options-panel" ).toggleClass( "open-panel", "close-panel", 800 );
		return false;
	});

	// Color Options
	$('.switch').click(function(){
		var title = $(this).attr('title');		
		$('#color-options').attr('href', 'css/colors/' + title + '.css');				
	  	return false;
    });	

	// Theme Options
	$('.theme').click(function(){
		var title = $(this).attr('title');		
		$('#theme-options').attr('href', 'css/theme/' + title + '.css');				
	  	return false;
    });	
