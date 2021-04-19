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

    
    $('#recalcBtn').on('click', function (e) {
        e.preventDefault();
        var mForm = $('#recalc').serialize();
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
});

// jQuery(document).ready(function () {

    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // // добавляем ajax-обработчик для обновления количества товара
    // $('#houseCounter').on('click', function (e) {
    //     let target_href = e.target;
    //     console.log(target_href.form);
    //     // if (target_href) {
    //     //     $.ajax({
    //     //         url: "" + target_href.name + "/" + target_href.value + "/",
    //     //         success: function (data) {
    //     //             console.log(data.tq);
    //     //             console.log(data.tc);
                    
    //     //         },
    //     //     });
    //     // }
    //     // event.preventDefault();
//     });
// });