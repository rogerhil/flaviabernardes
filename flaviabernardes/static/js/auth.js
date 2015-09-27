var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function login() {
    if (location.hash != '#login') return;
    $.ajax({
        url: '/login/json/',
        success: function (data) {
            if (!data.success) {
                alert(data.message);
                return
            }
            if (data.data.authenticated) {
                return;
            }
            $("#cover").html(data.data.content);
            $('#cover').fadeIn();
            $('#login button').click(loginSubmit);
        }
    });
}
function logout() {
    if (location.hash != '#logout') return;
    $.ajax({
        url: '/logout/json/',
        success: function (data) {
            if (!data.success) {
                alert(data.message);
                return
            }
            window.location = window.location.href.split('#')[0];
        }
    });
}

function setupLoginLogout() {
    login();
    logout();
};

window.onhashchange = setupLoginLogout;
setupLoginLogout();

function loginSubmit(e) {
    e.preventDefault();
    var formData = {
        username: $('#login input[name=username]').val(),
        password: $('#login input[name=password]').val(),
        csrfmiddlewaretoken: $('#login input[name=csrfmiddlewaretoken]').val(),
    };
    $.ajax({
        url: '/login/json/',
        type: 'post',
        dataType: 'json',
        data: formData,
        success: function (data) {
            if (!data.success) {
                alert(data.message);
                return
            }
            if (data.data) {
                $("#cover").html(data.data.content);
                $('#cover').fadeIn();
                $('#login button').click(loginSubmit);
                $('ul.errorlist').effect('bounce');
            } else {
                window.location = window.location.href.split('#')[0];
            }

        }
    });
}
