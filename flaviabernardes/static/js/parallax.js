$(window).ready(function () {
    $(".parallax").css("background-attachment", "fixed");
    $(window).resize(parallaxPosition);
    $(window).scroll(parallaxPosition);
    parallaxPosition();
});

function parallaxPosition(e) {
    var topWindow = $(window).scrollTop();
    var widthWindow = $(window).width();
    $(".parallax").each(function(i){
        var bp = $(this).css("background-position");
        var bgSize = $(this).attr('bg-size');
        var w = bgSize.split('x')[0];
        var h = bgSize.split('x')[1];
        var horp = (- (w - widthWindow) / 2) + 'px';
        var value = 80 - (topWindow / 2);
        $(this).css("background-position", horp + " " + value + "px");
        if (widthWindow > w) {
            $(this).css("background-size", widthWindow + "px");
        }
    });
}
