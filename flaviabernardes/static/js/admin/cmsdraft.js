
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
                $('.form-row').removeClass('errors');
                if ($(response).find('.errornote').length) {
                    $($(response).find('.errornote').clone().wrap('<p>').parent().html()).insertBefore($($('fieldset')[0]));
                    $(response).find('.form-row.errors').each(function () {
                        var id = $(this).find('label').attr('for');
                        $($(this).find('.errorlist').clone().wrap('<p>').parent().html()).insertBefore($("#" + id).parent());
                        $("#" + id).parent().parent().addClass('errors');
                    });
                    window.scrollTo(0, 0);
                    return;
                }
                window.location = path + 'preview/';
            }
        });
    });

    $('textarea.vLargeTextField').each(function () {
        tinymce.init({
            selector: "#" + $(this).attr('id'),
            external_plugins: {
                codemirror: "/static/tinymce/plugins/codemirror/plugin.js"
            },
            plugins: [
                "codemirror link image textcolor charmap visualblocks table imageupload"
            ],
            codemirror: {
                indentOnInit: true,
                path: 'codemirror-4.8',
                config: {
                    lineNumbers: true
                }
            },
            content_css: '/static/css/base.css,/static/css/blog.css',
            contentCss: '/static/css/base.css,/static/css/blog.css',
            relative_urls: false,
            height: 600,
            extended_valid_elements: '*[*],script[charset|defer|language|src|type]',
            toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | forecolor link | table | image imageupload | code",
        });
        window.setTimeout(function () {
            $('.mce-edit-area').css('width', '960px').css('padding', '0 100px').css('margin', '0 auto');
        }, 1000);

    });
});
