function setupNewsletter() {
    $('#newsletter').ajaxForm({
        beforeSubmit: function(arr, $form, options) {
            $('#cover').fadeIn();
            fbq('track', 'Lead');
        },
        success: function (response, status, xhr, $form) {
            $('#cover').fadeOut();
            if (response.success) {
                var email = $('#newsletter input[type=email]').val();
                var msg = 'Please confirm your subscription in the email message that was just sent to ' + email;
                $("#newsletter-wrap").html('<div class="center" style="color: #A50017">' + msg + '.</div>').css('padding', '5px');
                $("#newsletter-wrap").effect('highlight', 2000, function () {
                    $("#newsletter-wrap").effect('highlight', 2000);
                });
            } else {
                $('#newsletter-wrap').html(response.html);
                setupNewsletter();
            }

        }
    });
}

setupNewsletter();
