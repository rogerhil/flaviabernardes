
$(window).ready(function () {
    $("#changelist-form tr th a").each(function () {
        var href = $(this).attr('href');
        if (href.indexOf('?o=') != -1) return;
        var pid = href.split('/')[4];
        var redirect = '/admin/blog/draft/';
        $(this).attr('href', 'javascript:;');
        $(this).click(function () {
            $.ajax({
                url: '/admin/blog/' + pid + '/new-draft/',
                type: 'post',
                dataType: 'json',
                success: function (data) {
                    if (data.success) {
                        window.location = redirect + data.data.draft_id + '/';
                    } else {
                        alert(data.message);
                    }
                }
            });
        });
    });

});
