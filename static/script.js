

  $(window).scroll(function () { 
    $('#nav-placeholder').toggleClass('scrolled',$(this).scrollTop() > 100)
    $('#nav-placeholder').toggleClass('title',$(this).scrollTop() > 100)
    $('#nav-placeholder').toggleClass('scrolled1',$(this).scrollTop() > 450)
    $('#nav-placeholder').toggleClass('title',$(this).scrollTop() > 450)





});