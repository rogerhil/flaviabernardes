var headerBgColor;

$(window).ready(function () {
    var isiOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    headerBgColor = $('#header').css('background-color');
    $("#artworks .parallax").css("background-attachment", "fixed");
    if (isiOS) {
        //parallaxPosition();
        return;
    }
    $(window).resize(parallaxPosition2);
    $(window).scroll(parallaxPosition2);
    parallaxPosition2();
});

function parallaxPosition2(e) {
    //var topWindow = $(window).scrollTop();
    //var widthWindow = $(window).width();
    var headerHeight = Number($('#header').css('height').replace('px', ''));
    $("#artworks .parallax").each(function(i) {
        var topWindow = $(window).scrollTop();
        //var bottomWindow = $(window).scrollBottom();
        var widthWindow = $(window).width();
        var heightWindow = $(window).height();
        if (!$(this).attr('bg')) {
            $(this).attr('bg', $(this).css('background-image'));
        }
        var bp = $(this).css("background-position");
        var bgSize = $(this).attr('bg-size');
        var w = bgSize.split('x')[0];
        var h = bgSize.split('x')[1];
        var horp = (- (w - widthWindow) / 2) + 'px';
        var height = Number($(this).position().top);
        var value = headerHeight / 2 + height / 2 - (topWindow / 6);
        if (widthWindow > w) {
            horp = '0px';
            //$(this).css("background-size", "cover");
        }
        horp = $(this).parent().position().left;
        horp = horp + ((Number($(this).css('width').replace('px', '')) - w) / 2);
        var hh = Number($(this).parent().position().top) - topWindow;
        //if (hh < heightWindow)
        //hh = hh + hh * 0.5;
        $(this).css("background-position", horp + "px " + (value + hh) + "px");
        if (widthWindow > w) {
            //$(this).css("background-size", widthWindow + "px");
        }
        //$(this).css("background-size", "640px 600px");
    });
}
