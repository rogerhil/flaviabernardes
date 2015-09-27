function scrollFixedElements() {
    var $sm = $('.scroll-fixed');
    if (window.innerWidth < 645) {
        $sm.css('position', 'static');
        $sm.css('top', '0px');
        return;
    }
    console.log(window.innerWidth);
    var $anchor = $('#' + $sm.attr('anchor'));
    var height = $sm.css('height');
    var margin = $sm.css('margin');
    var stop = $anchor.offset().top;
    var wtop = $(window).scrollTop();
    var fixat = Number($sm.attr('fixat'));
    if ((wtop + fixat) > stop) {
        $sm.css('position', 'fixed');
        $sm.css('top', fixat + 'px');
        $anchor.css('height', height);
        $anchor.css('margin', margin);
    } else {
        $sm.css('position', 'static');
        $sm.css('top', '0px');
        $anchor.css('height', 0);
        $anchor.css('margin', 0);
    }
}

$(window).load(function () {
    scrollFixedElements();
    $(window).scroll(function () {
        scrollFixedElements();
    });
    $(window).resize(function () {
        scrollFixedElements();
    });
});
