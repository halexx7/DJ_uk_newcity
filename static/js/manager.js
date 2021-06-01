jQuery(document).ready(function(){

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
            return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);

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

    //Ловим событие формы 1
    $('#houseCounterBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#houseCounterForm').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (e) {
        	    console.log(e);
            },
            error: function (e) {
                console.log(e);
            }
        });
    });

    //Ловим событие формы 2
    $('#recalcBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#recalcForm').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
        	    console.log(data.responseText);
            },
            error: function (data) {
                console.log(data.responseText);
            }
        });
    });
});
