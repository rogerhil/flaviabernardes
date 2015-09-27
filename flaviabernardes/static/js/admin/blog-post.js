
$(window).ready(function () {
    $("#changelist-form tr").each(function () {
        if (!$(this).find('td').length) return;
        var slug = $($(this).find('td')[1]).html();
        var redirect = '/admin/blog/draft/';
        $($(this).find('a')[0]).attr('href', '/blog/' + slug + '/');
    });

    $("#changelist-form a.modify").each(function () {
        var pid = $(this).attr('pid');
        var redirect = '/admin/blog/draft/';
        $(this).click(function () {
            $.ajax({
                url: '/admin/blog/post/' + pid + '/new-draft/',
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