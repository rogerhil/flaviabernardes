function scrollFixedElements() {
    var $sm = $('.scroll-fixed');
    if (window.innerWidth < 645) {
        $sm.css('position', 'static');
        $sm.css('top', '0px');
        return;
    }
    var $anchor = $('#' + $sm.attr('anchor'));
    var height = $sm.css('height');
    var margin = $sm.css('margin');
    if (!$anchor.offset()) {
        return;
    }
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
    var isiOS = /iPhone|iPad|iPod/i.test(navigator.userAgent);
    if (isiOS) {
        return;
    }
    scrollFixedElements();
    $(window).scroll(function () {
        scrollFixedElements();
    });
    $(window).resize(function () {
        scrollFixedElements();
    });
});
