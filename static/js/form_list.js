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
        	    console.log('hello');
            },
            error: function (e) {
                console.log('world');
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

    //Ловим событие формы COUNTERFORM
    $('#counterBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#counterForm').serialize();
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                $('form input[name="col_water"], form input[name="hot_water"]').val('');
                $('#counterBtn').before('<div class="flex-fill  alert  alert-success  mt-3  mb-5" id="successAlert"><p>Данные успешно приняты!</p></div>');
                setTimeout(function(){
                    $('#successAlert').remove();
                }, 50000);
            },
            error: function (data) {
                $('form input[name="col_water"], form input[name="hot_water"]').val('');
                $('#counterBtn').before('<div class="flex-fill  alert  alert-danger  mt-3  mb-5" id="successAlert"><p>Что-то пошло не так! Попробуйте чуть позже!</p></div>');
                setTimeout(function(){
                    $('#successAlert').remove();
                }, 50000);
            }
        });
    });
});
