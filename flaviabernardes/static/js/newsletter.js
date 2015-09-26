
$(window).ready(function () {
    setupNewsletter();
});

function setupNewsletter() {
    $('#newsletter').ajaxForm({
        success: function (response, status, xhr, $form) {
            if (response.success) {
                alert('SUCESS');
            } else {
                $('#newsletter-wrap').html(response.html);
                setupNewsletter();
            }

        }
    });
}
