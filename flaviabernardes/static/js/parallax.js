var headerBgColor;

$(window).ready(function () {
    var isiOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    if (isiOS) {
        return;
    }
    headerBgColor = $('#header').css('background-color');
    $(".parallax").css("background-attachment", "fixed");
    $(window).resize(parallaxPosition);
    $(window).scroll(parallaxPosition);
    parallaxPosition();
});

function parallaxPosition(e) {
    //var topWindow = $(window).scrollTop();
    //var widthWindow = $(window).width();
    if (!$('#header').length) {
        return;
    }
    var headerHeight = Number($('#header').css('height').replace('px', ''));
    $(".parallax").each(function(i) {
        var topWindow = $(window).scrollTop();
        //var bottomWindow = $(window).scrollBottom();
        var widthWindow = $(window).width();
        if (!$(this).attr('bg')) {
            $(this).attr('bg', $(this).css('background-image'));
        }
        var bp = $(this).css("background-position");
        var bgSize = $(this).attr('bg-size');
        var w = bgSize.split('x')[0];
        var h = bgSize.split('x')[1];
        var horp = (- (w - widthWindow) / 2) + 'px';
        var height = Number($(this).position().top);
        var value = headerHeight / 2 + height / 2 - (topWindow / 2);
        if (widthWindow > w) {
            horp = '0px';
            $(this).css("background-size", "cover");
        }
        $(this).css("background-position", horp + " " + value + "px");
        if (widthWindow > w) {
            $(this).css("background-size", widthWindow + "px");
        }
    });
}
