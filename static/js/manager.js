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

    // Выводим сообщение в соответствующий Alert bootstrap
    function displayCounterAlert(say, typeAlert, time, target){
        $('#successAlert').remove();
            $('form input[name="col_water"], form input[name="hot_water"]').val('');
            setTimeout(function(){
                $('#successAlert').remove();
            }, time);
    };

    //Ловим нажатие кнопки формирования платежки
    $('#formationPayBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#formationPayForm').serialize();
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (e) {
                $(`.category__form`).addClass(`d-flex  flex-column  align-items-center`);
                $(`.category__form`).html(`<div class="flex-fill  alert  alert-success  mt-5  mb-3" id="successAlert">
                <p>Платежки успешно сформированы!</p>
                </div>
                <div><a class="btn btn-link  nav-link" role="button" onclick="javascript:history.back(); return false;">Вернуться на главную</a></div>
                `);
            },
            error: function (e) {
                $(`.category__form`).addClass(`d-flex  flex-column  align-items-center`);
                $(`.category__form`).html(`<div class="flex-fill  alert  alert-danger  mt-5  mb-3" id="successAlert">
                <p>Что-то пошло не так! Попробуйте чуть позже!</p>
                </div>
                <div><a class="btn btn-link  nav-link" role="button" onclick="javascript:history.back(); return false;">Вернуться на главную</a></div>
                `);
            },
        });
    });
});
