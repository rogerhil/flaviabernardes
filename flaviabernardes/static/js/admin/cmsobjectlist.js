
function newDraft(model, draft_model, obj_id) {
    var app = window.location.pathname.split('/')[2];
    var basepath = '/admin/' + app +  '/' + model + '/';
    var redirect = '/admin/' + app +  '/' + draft_model + '/';
    $('#cover').fadeIn();
    $.ajax({
        url: basepath + obj_id + '/new-draft/',
        type: 'post',
        dataType: 'json',
        success: function (data) {
            //$('#cover').fadeOut();
            if (data.success) {
                window.location = redirect + data.data.draft_id + '/';
            } else {
                $('#cover').fadeOut();
                alert(data.message);
            }
        }
    });
}

$(window).ready(function () {
    $("#changelist-form tr").each(function () {
        if (!$(this).find('td').length) return;
        var url = $($(this).find('td a.modify')).attr('view-url');
        $($(this).find('a')[0]).attr('href', url);
    });

    $("#changelist-form a.modify").each(function () {
        var obj_id = $(this).attr('obj_id');
        var model = $(this).attr('model');
        var draft_model = $(this).attr('draft-model');
        $(this).click(function () {
            newDraft(model, draft_model, obj_id);
        });
    });
});
