
$(window).ready(function () {
    var path = window.location.pathname;
    var $preview = $('<input id="preview" type="submit" value="Save and Preview" name="_continue" style="color: blue;">');
    ($("div.submit-row input")[1]).remove();
    ($("div.submit-row input")[0]).remove();
    $preview.insertBefore($($("div.submit-row input")[0]));

    $preview.click(function () {
        $('#content-main form').ajaxForm({
            beforeSubmit: function(arr, $form, options) {
                $('#cover').fadeIn();
            },
            success: function (response, status, xhr, $form) {
                $('#cover').fadeOut();
                window.location = path + 'preview/';
            }
        });
    });

    $('textarea.vLargeTextField').each(function () {
        tinymce.init({
            selector: "#" + $(this).attr('id'),
            plugins: [
                "link image textcolor"
            ],
            toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | forecolor link image",
        });
    });
});
