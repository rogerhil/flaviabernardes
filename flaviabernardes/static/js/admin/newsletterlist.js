
$(window).ready(function () {
    $('textarea.vLargeTextField').each(function () {
        tinymce.init({
            selector: "#" + $(this).attr('id'),
            plugins: [
                "link image textcolor charmap visualblocks table code imageupload"
            ],
            //content_css: '/static/css/base.css',
            relative_urls: false,
            height: 500,
            toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | forecolor link | table | image imageupload",
        });
        window.setTimeout(function () {
            $('.mce-edit-area').css('width', '960px').css('padding', '0 100px').css('margin', '0 auto');
        }, 500);

    });
});
