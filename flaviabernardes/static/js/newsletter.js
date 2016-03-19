function setupNewsletter() {
    $('.newsletter').ajaxForm({
        beforeSubmit: function(arr, $form, options) {
            $('#cover').fadeIn();
            fbq('track', 'Lead');
        },
        success: function (response, status, xhr, $form) {
            $('#cover').fadeOut();
            var $par = $form.parent().parent();
            var $wrap = $par.find(".newsletter-wrap");
            if (response.success) {
                var email = $form.find('input[type=email]').val();
                var msg = 'Please confirm your subscription in the email message that was just sent to ' + email;
                $wrap.html('<div class="center" style="color: #A50017">' + msg + '.</div>').css('padding', '5px');
                $wrap.effect('highlight', 2000, function () {
                    $wrap.effect('highlight', 2000);
                });
            } else {
                if (response.errors.__all__) {
                    $form.html(response.html);
                    $form.find('ul').remove();
                    if ($form.parents('#top-bar').length) {
                        window.setTimeout(function () {
                           $('#top-bar .top-bar-close').trigger('click');
                        }, 5000);
                    }
                } else {
                    $form.html(response.html);
                    setupNewsletter();
                }
            }
        }
    });
}

setupNewsletter();
