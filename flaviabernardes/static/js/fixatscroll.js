$(window).load(function () {
    function scrollFixedElements() {
        var $sm = $('.scroll-fixed');
        var stop = $('#' + $sm.attr('anchor')).offset().top;
        var wtop = $(window).scrollTop();
        var fixat = Number($sm.attr('fixat'));
        if ((wtop + fixat) > stop) {
            $sm.css('position', 'fixed');
            $sm.css('top', fixat + 'px');
        } else {
            $sm.css('position', 'static');
            $sm.css('top', '0px');
        }
    }
    scrollFixedElements();
    $(window).scroll(function () {
        scrollFixedElements()
    });
    $(window).resize(function () {
        scrollFixedElements()
    });

});
