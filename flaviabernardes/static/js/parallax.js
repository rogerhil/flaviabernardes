var headerBgColor;

$(window).ready(function () {
    var isiOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    headerBgColor = $('#header').css('background-color');
    $(".parallax").css("background-attachment", "fixed");
    if (isiOS) {
        parallaxPosition();
        return;
    }
    $(window).resize(parallaxPosition);
    $(window).scroll(parallaxPosition);
    parallaxPosition();
});

function parallaxPosition(e) {
    var topWindow = $(window).scrollTop();
    var widthWindow = $(window).width();
    var headerHeight = Number($('#header').css('height').replace('px', ''));
    $(".parallax").each(function(i) {
        if (!$(this).attr('bg')) {
            $(this).attr('bg', $(this).css('background-image'));
        }
        var bp = $(this).css("background-position");
        var bgSize = $(this).attr('bg-size');
        var w = bgSize.split('x')[0];
        var h = bgSize.split('x')[1];
        var horp = (- (w - widthWindow) / 2) + 'px';
        var value = headerHeight - (topWindow / 2);
        $(this).css("background-position", horp + " " + value + "px");
        //if (topWindow > 300) {
        //    $('#header').css('background-color', headerBgColor);
        //    $(this).css('background-image', '');
        //} else {
        //    $('#header').css('background-color', 'white');
        //    $(this).css('background-image', $(this).attr('bg'));
        //}
        if (widthWindow > w) {
            $(this).css("background-size", widthWindow + "px");
        }
    });
}
