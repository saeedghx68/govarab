 
/*-----------------------------------
 Quick Mobile Detection
 -----------------------------------*/

 var isMobile = {
    Android: function() {
      "use strict";
      return navigator.userAgent.match(/Android/i);
    },
    BlackBerry: function() {
      "use strict";
      return navigator.userAgent.match(/BlackBerry/i);
    },
    iOS: function() {
      "use strict";
      return navigator.userAgent.match(/iPhone|iPad|iPod/i);
    },
    Opera: function() {
      "use strict";
      return navigator.userAgent.match(/Opera Mini/i);
    },
    Windows: function() {
      "use strict";
      return navigator.userAgent.match(/IEMobile/i);
    },
    any: function() {
      "use strict";
      return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
    }
};

/*-----------------------------------
 Page PreLoader
 -----------------------------------*/

$(window).load(function() {
  "use strict";
  $(".loader").delay(800).fadeOut();
  $("#preloader").delay(1200).fadeOut("slow");
});

 /*-----------------------------------
 Home Section Text Slider
 -----------------------------------*/

 $(window).load(function(){
  "use strict";
  $('.header-text').flexslider({
  animation: "slide",
	selector: ".text-slider .text-slides",
  slideshowSpeed: 5000,  
	controlNav: false,
	directionNav: false ,
	direction: "vertical",
      start: function(slider){
       $('body').removeClass('loader'); 
      }
  });
 });

 /*-----------------------------------
 Full Screen Home Section Slider
 -----------------------------------*/

$(window).load(function(){
  "use strict";
  $('#slides').superslides({
    animation: 'fade',
    play: 7000,
    animation_speed: 3000
  });
});

/*-----------------------------------
Slow Zoom Header Image
-----------------------------------*/

$(window).load(function(){
  "use strict";
  $(".zoom-container").find('img').addClass("zoom-in"); // add class
  var tid = setTimeout(zoomLoop, 90000); // set timer

  function zoomLoop() {
    "use strict";
    $(".zoom-container img").fadeOut(2000, function() { // fade out
      $(".zoom-container").find('img').removeClass("zoom-in");
    });
    $(".zoom-container img").fadeIn(1500, function() { // fade in
      $(".zoom-container").find('img').addClass("zoom-in");
    });
    tid = setTimeout(zoomLoop, 90000); // reset timer
  }
});

/*-----------------------------------
Full Screen Headers
 -----------------------------------*/

$(function(){
"use strict";
  $('.alt-header').css({'height':($(window).height())+'px'});
  $(window).resize(function(){
    $('.alt-header').css({'height':($(window).height())+'px'});
  });
});

/*-----------------------------------
Navigation Scroll Page
-----------------------------------*/

$(function() {
  "use strict";
  $('.scroll').bind('click', function(event) {
    var $anchor = $(this);
    var headerH = $('#navigation').outerHeight();
    $('html, body').stop().animate({
      scrollTop : $($anchor.attr('href')).offset().top - headerH + "px"
    }, 1200, 'easeInOutExpo');

    event.preventDefault();
  });
});

/*-----------------------------------
Show Active Navigation
-----------------------------------*/

var sections = $('.section'),
    links = $('.scroll.link');

$(window).scroll(function() {
  "use strict";
  var currentPosition = $(this).scrollTop();
  links.removeClass('selected');
  
  sections.each(function() {
      var top = $(this).offset().top - 75,
          bottom = top + $(this).height();
      
      if (currentPosition >= top && currentPosition <= bottom) {
          $('a[href="#' + this.id + '"]').addClass('selected');
      }
  }); 
});

/*-----------------------------------
Show Navigation Bar on Scroll Down
-----------------------------------*/

$(document).ready(function () {
  "use strict";
  var menu = $('#navigation');

  $(window).scroll(function () {
    "use strict";
    var y = $(this).scrollTop();
    var z = $('#about').offset().top - 250;

    if (y >= z) { menu.removeClass('hide-nav').addClass('show-nav');}
    else { menu.removeClass('show-nav').addClass('hide-nav'); }
  });
});

/*-----------------------------------
Menu for mobile devices
-----------------------------------*/

$('.mobile-nav-button').click(function() {
  "use strict";
  $(".nav-menu").slideToggle("8000");
 });
$('.nav a').click(function () {
  "use strict";
  if ($(window).width() < 960) {
      $(".nav-menu").slideToggle("2000")}
});

/*-----------------------------------
Slider for Testimonials
-----------------------------------*/
  
$(window).load(function(){ 
  "use strict";
  $('.container').flexslider({
  animation: "fade",
  selector: ".testimonial-slider .t-slide",
  controlNav: false,
  directionNav: true ,
  slideshowSpeed: 8000
    });
});

/*-----------------------------------
Parallax Sections (disabled on mobile)
-----------------------------------*/

$(document).ready(function(){
  "use strict";
  if(!isMobile.any()) {
    $('.parallax1').parallax("50%", 0.5);
    $('.parallax2').parallax("50%", 0.5);
    $('.parallax3').parallax("50%", 0.5);
    $('.parallax4').parallax("50%", 0.5);
    $('.parallax5').parallax("50%", 0.5);
    $('.parallax6').parallax("50%", 0.5);
  }
});


/*-----------------------------------
Fit Videos
-----------------------------------*/

$(window).load(function(){
  "use strict";
  $(".fit-vids").fitVids();
 });


/*-----------------------------------
Isotope Portfolio
-----------------------------------*/

$(window).load(function() {
  "use strict";
        
  var $container = $('.portfolio-items');

  $container.isotope({
    resizable: false, 
    itemSelector : '.item'
  });
        
  var $optionSets = $('#options .option-set'),
      $optionLinks = $optionSets.find('a');

  $optionLinks.click(function(){
    var $this = $(this);
    if ( $this.hasClass('selected') ) {
      return false;
    }
    var $optionSet = $this.parents('.option-set');
    $optionSet.find('.selected').removeClass('selected');
    $this.addClass('selected');

    var options = {},
        key = $optionSet.attr('data-option-key'),
        value = $this.attr('data-option-value');
    value = value === 'false' ? false : value;
    options[ key ] = value;
    if ( key === 'layoutMode' && typeof changeLayoutMode === 'function' ) {
      changeLayoutMode( $this, options )
    } else {
      $container.isotope( options );
    }
    return false;
  });

  // Project Expander
  var loader = $('.item-expander');
  
  $('.expander').on('click', function(e){
    e.preventDefault();
    e.stopPropagation();
    var url = $(this).attr('href');

    loader.slideUp(function(){
      $.get(url, function(data){
        var portfolioContainer = $('#portfolio-container');
        var topPosition = portfolioContainer.offset().top;
        var bottomPosition = topPosition + portfolioContainer.height();
        $('html,body').delay(600).animate({ scrollTop: topPosition }, 800);
        var container = $('#item-expander>div', loader);
        
        container.html(data);
         $(".fit-vids").fitVids();
        $('.project').flexslider({
              animation: "fade",
          selector: ".project-slides .slide",
          controlNav: true,
          directionNav: true ,
          slideshowSpeed: 5000,  
            });
        
      //   container.fitVids();
        loader.slideDown(function(){
          if(typeof keepVideoRatio == 'function'){
            keepVideoRatio('.project-video > iframe');
          }
        }).delay(1000).animate({opacity:1}, 200);
      });
    });
  });
    
    $('.close', loader).on('click', function(){
      loader.delay(300).slideUp(function(){
        var container = $('#item-expander>div', loader);
        container.html('');
        $(this).css({opacity:0});
        
      });
      var portfolioContainer = $('#portfolio-container');
        var topPosition = portfolioContainer.offset().top;
        $('html,body').delay(0).animate({ scrollTop: bottomPosition - 50}, 500);
    });

});

/*-----------------------------------
PrettyPhoto
-----------------------------------*/

$(document).ready(function(){
  "use strict";
    $("a[data-rel^='prettyPhoto']").prettyPhoto({
        deeplinking: false,
        social_tools: false
    });
  });

/*-----------------------------------
Animated Elements
-----------------------------------*/

$(document).ready(function($) {
  "use strict";
  $('.animated').appear(function() {
      var elem = $(this);
      var animate = elem.data('animate');
      if ( !elem.hasClass('visible') ) {
        var animateDelay = elem.data('animate-delay');
          if ( animateDelay ) {
              setTimeout(function(){
                  elem.addClass( animate + " visible" );
              }, animateDelay);
          } else {
              elem.addClass( animate + " visible" );
          }
      }
  });
});

/*-----------------------------------
Counter
-----------------------------------*/

$(function() {
  "use strict";
  $(".count").appear(function(){
  $('.count').each(function(){
      var count = $(this).attr('data-to');
  $(this).find('.count-number').delay(6000).countTo({
        from: 50,
        to: count,
        speed: 3000,
        refreshInterval: 50,  
      });  
    });
  });
});

/*-----------------------------------
Tooltips
-----------------------------------*/

$(document).ready(function() {
  "use strict";
  $(".tipped").tipper({
    direction: "top"
  });
}); 

/*-----------------------------------
Accordion
-----------------------------------*/

$(document).ready(function() {
  "use strict";
 
  //Accordion button
  $('div.accordion-button').click(function() {
    $('div.accordion-content').slideUp('normal');
    if ( $('div.accordion-button i').hasClass('fa-arrow-circle-o-down') ) {
      $('div.accordion-button i').removeClass('fa-arrow-circle-o-down').addClass('fa-arrow-circle-o-right');
    }
    $(this).find('i').toggleClass('fa-arrow-circle-o-right').toggleClass('fa-arrow-circle-o-down');
    $(this).next().slideDown('normal');

  });
 
  //initial state 
  $("div.accordion-content").hide();
  $('div.accordion-content.active').slideDown('normal');
 
});

/*-----------------------------------
Skill Bar
-----------------------------------*/

$(document).ready(function(){
  "use strict";
  $('.skillbar').appear(function() {
    $(this).find('.skillbar-bar').animate({
      width:$(this).attr('data-percent')
    },3000);
  });
});

/*-----------------------------------
Full Width Video
-----------------------------------*/

$(function(){
  "use strict";
  $(".player").mb_YTPlayer();
});

/*-----------------------------------
Close Button for Alert Boxes
-----------------------------------*/

$('.close-alert').click(
  function(){
    "use strict";
    $(this).closest('.alert').fadeOut(1000);
  });

/*-----------------------------------
Contact Form
-----------------------------------*/

$(document).ready(function ($) { 
  "use strict";

  $('#submit').click(function(){ 

    $('.error').hide(); 

    var name = $('input#name').val();
    var email = $('input#email').val();
    var phone = $('input#phone').val();
    var email_compare = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/; // compare to email input
    var phone_compare = /^[0-9-+]+$/; // compare to phone input

    if (name == "" || name == " ") {
      $('#error-name').fadeIn('slow');
      return false;

    } else if (email == "" || email == " ") {
      $('#error-email').fadeIn('slow');
      return false;

    } else if (!email_compare.test(email)) {
      $('#error-valid-email').fadeIn('slow');
      return false;

    } else if (!phone_compare.test(phone)) {
      $('#error-valid-phone').fadeIn('slow');
      return false;
    }

    var data_string = $('#contact-us').serialize(); 

    $.ajax({
      type: "POST",
      url: $('#contact-us').attr('action'),
      data: data_string,
      timeout: 6000,
      error: function(request,error) {
        if (error == "timeout") {
          $('#error-timedout').slideDown('slow');
        }
        else {
          $('#error-state').slideDown('slow');
        }
      },
      success: function() {
        $('#email-success').slideDown('slow');
        $("#contact-us").trigger('reset');
      }
    });

    return false;
  });
});


 /*-----------------------------------
Google Map
-----------------------------------*/

$(document).ready(function() {
  "use strict";

  // Map Coordinates
  var latlng = new google.maps.LatLng(30.307992, -97.752033);

  // Map Options
  var myOptions = {
    zoom: 15,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: true,
    scrollwheel: false,
  };

  var map = new google.maps.Map(document.getElementById('google-map'), myOptions);

  // Marker Image
  var image = 'images/marker.png';
  
  //  Start Marker    
  var myLatlng = new google.maps.LatLng(30.307863, -97.752329);

  // Marker Text 
   var contentString = '<div id="map-tooltip"><h5>Our Office Location</h5><p>Come see us!</p></div>';
  
  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: 'Hello World!',
      icon: image
    });

  var infowindow = new google.maps.InfoWindow({
    content: contentString
    });
    
   google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
    });

   // End Marker

})