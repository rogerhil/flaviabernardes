
$(window).ready(function () {
    var draftId = window.location.pathname.split('/')[4];
    var $preview = $('<input id="preview" type="submit" value="Save and Preview" name="_continue" style="color: blue;">');
    ($("div.submit-row input")[1]).remove();
    ($("div.submit-row input")[0]).remove();
    $preview.insertBefore($($("div.submit-row input")[0]));

    $preview.click(function () {
        $('#draft_form').ajaxForm({
            success: function (response, status, xhr, $form) {
                window.open('/admin/blog/draft/' + draftId + '/preview/');
            }
        });
    });

    tinymce.init({
        selector: "#id_text"
    });
});
