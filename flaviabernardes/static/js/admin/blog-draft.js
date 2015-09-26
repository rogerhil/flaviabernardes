
$(window).ready(function () {
    var draftId = window.location.pathname.split('/')[4];
    var $publish = $('<input id="publish" type="button" value="Publish" style="color: green; font-weight: bold;">');
    var $preview = $('<input id="preview" type="submit" value="Save and Preview" name="_continue" style="color: blue;">');
    ($("div.submit-row input")[1]).remove();
    $preview.insertBefore($($("div.submit-row input")[0]));
    $publish.insertBefore($($("div.submit-row input")[0]));
    $publish.click(function () {
        if (confirm("Are you sure you want to publish this draft?")) {
            $('#draft_form').ajaxForm({
                success: function (response, status, xhr, $form) {
                    console.log(status);
                    $.ajax({
                        url: '/admin/blog/draft/' + draftId + '/publish/',
                        type: 'post',
                        dataType: 'json',
                        success: function (data) {
                            console.log(data);
                        }
                    });
                }
            });
            $('#draft_form').trigger('submit');
        }
    });

    tinymce.init({
        selector: "#id_text"
    });

});
