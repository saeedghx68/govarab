
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
  var logo = $('#logo');

  $(window).scroll(function () {
    "use strict";
    var y = $(this).scrollTop();
    var z = $('#about').offset().top - 250;

    if (y >= z) {
        menu.removeClass('hide-nav').addClass('show-nav');
        logo.removeClass('hide-nav').addClass('show-nav');
    }
    else {
        menu.removeClass('show-nav').addClass('hide-nav');
        logo.removeClass('show-nav').addClass('hide-nav');
    }
  });
});