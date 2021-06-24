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

    // Выводим сообщение в соответствующий Alert bootstrap
    function displayCounterAlert(say, typeAlert, time, target){
        $('#successAlert').remove();
            $('form input[name="col_water"], form input[name="hot_water"]').val('');
            $(`#${target}`).before(`<div class="flex-fill  alert  alert-${typeAlert}  mt-3  mb-5" id="successAlert"><p>${say}</p></div>`);
            setTimeout(function(){
                $('#successAlert').remove();
            }, time);
    };


    // MANAGER_LIST
    //Ловим событие формы CURRENT
    $('#currentCountBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#house_count_form').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });

    //Ловим событие формы RECALCULATIONS
    $('#recalcBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#recalculations_form').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });

    //Ловим событие формы PRIVILEGE
    $('#privilegeBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#privilege_form').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });

    //Ловим событие формы SUBSIDIES
    $('#subsidiesBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#subsidies_form').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });

    //Ловим событие формы PAYMENTS
    $('#paymentsBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#payments_form').serialize();
        console.log(mForm);
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });


    // USER_LIST
    //Ловим событие формы COUNTERFORM
    $('#counterBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#counterForm').serialize();
        $.ajax({
            type : 'POST',
            data: mForm,
            success: function (data) {
                say = `Данные успешно приняты!`;
                time = 15000;
                typeAlert = `success`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            },
            error: function (data) {
                say = `Что-то пошло не так! Попробуйте чуть позже!`;
                time = 15000;
                typeAlert = `danger`;
                displayCounterAlert(say, typeAlert, time, e.target.id);
            }
        });
    });
});
