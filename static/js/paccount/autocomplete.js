async function autocomplete(inp) {
    let arr = [];
    let currentFocus, a, b, i, body, val = inp.value;
    let request = {
        url: `${window.location.href}autocomplete/`,
        csrf: getCookieCSRF(),
    }

    // Функция парсинга формы и отправки данных на сервис
    async function saveDataForm(event, formID, reDrawDiv) {
        let reqData;
        event.preventDefault();
        
        // Парсит данные с формы и возвращает объект -> {'csrf': token, 'body': body}
        function parceFormData (formData) {
            let str = '';
            for(let [name, value] of formData) {
                str += `${name}=${value}&`};
            return str.slice(0, -1)}
        
        // Очищаем инпуты
        function clearInput(arr) {
            arr.forEach(element => {
                element.value = '';
            });};
        
        // Выводим сообщение в соответствующий Alert bootstrap
        function displayCounterAlert(say, typeAlert, time, target){
            try {
                // Если элемента нет пролетаем дальше без ошибки
                document.querySelector('#successAlert').remove();
            } catch{ }
    
            // Чистим поля после отправики данных
            clearInput(document.querySelectorAll('div.clear__input input'));
            clearInput(document.querySelectorAll('form select'));
    
            // Создаем новый div
            let helper = document.createElement('div');
            let html = `<div class="flex-fill  alert  alert-${typeAlert}  mt-3  mb-5" id="successAlert"><p>${say}</p></div>`;
            helper.innerHTML = html;
            document.querySelector(`#${target}`).before(helper);
    
            // Таймер показа сообщения
            setTimeout(function(){
                document.querySelector('#successAlert').remove();
            }, time);};
    
        const formData = new FormData(document.getElementById(formID));
        if (formData.has('user')) {
            const key = formData.get('user').slice(0 ,6);
            formData.append('personalacc', key);
        }

        request.body = parceFormData(formData);
        const response = await fetch(window.location.href, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRFToken': request.csrf,
            },
            body: request.body})
    
        if (response.ok) {
            let json = await response.json();
            let say = `Данные успешно приняты!`;
            let time = 15000;
            let typeAlert = `success`;
            displayCounterAlert(say, typeAlert, time, event.target.id);
            let one = document.getElementById(reDrawDiv);
            one.innerHTML = json.instance;

        } else {
            let say = `Что-то пошло не так! Попробуйте чуть позже!`;
            let time = 15000;
            let typeAlert = `danger`;
            displayCounterAlert(say, typeAlert, time, event.target.id);
        }
    }

    // Асинхронный запрос на сервер
    async function getAjaxRequest(body) {
        const responce = await fetch(request.url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRFToken': request['csrf']
            },
            body: JSON.stringify(body)
        })

        if (responce.ok) {
            let json = await responce.json();
            return json;
        }
    };

    // Проверяем добавлен ли уже элемент - Выпадающий список
    a = document.getElementById(`${inp.id}-autocomplete-list`);
    if (!a) {
        // Если нет, то создаем
        a = document.createElement("DIV");
        a.setAttribute("id", inp.id + "-autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        inp.parentNode.appendChild(a);
    } else {
        // если да, то чистим
        // a.innerHTML = '';
        while (a.firstChild) {
            a.removeChild(a.firstChild);
        }
    }

    // Если короче 3 символов, ничего не делаем
    if (!val || (val.length < 3) || !a) { return false;}
    currentFocus = -1;

    body = {type: inp.id, value: inp.value}
    const responce = await getAjaxRequest(body);

    // arr = []
    for (let [key, value] of Object.entries(responce.value)) {
        arr.push(`${key} - ${value}`);
    }

    for (i = 0; i < arr.length; i++) {
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            b = document.createElement("DIV");
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";

            b.addEventListener("click", function(e) {
                inp.value = e.target.textContent;
                closeAllLists(a);
            });
            a.appendChild(b);
        }
    };

    inp.addEventListener("keydown", function(e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            currentFocus++;
            addActive(x);
        } else if (e.keyCode == 38) { //up
            currentFocus--;
            addActive(x);
        } else if (e.keyCode == 13) {
            e.preventDefault();
            if (currentFocus > -1) {
                if (x) x[currentFocus].click();
            }
        }
    });

    // Получаем csrf из cookie если нет формы
    function getCookieCSRF() {
        let matches = document.cookie.match(new RegExp(
            "(?:^|; )" + "csrftoken".replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
        ));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }

    function addActive(x) {
        if (!x) return false;
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        x[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(x) {
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists(a) {
        const els = Array.prototype.slice.call(a.childNodes);
        els.forEach(function(elem, idx) {
            elem.parentNode.removeChild(elem);
          });
        }

    document.addEventListener("click", function (e) {
        closeAllLists();
    });
}


//Ловим событие формы PAYMENTS
document.getElementById("paymentsBtn").addEventListener('click', event => {
    let formID = 'payments_form';
    let reDrawDiv = 'paymentsList';
    saveDataForm(event, formID, reDrawDiv).then()});

//Ловим событие формы CURRENT
document.getElementById("currentCountBtn").addEventListener('click', event => {
    let formID = 'house_count_form';
    let reDrawDiv = '.house-current_list';
    saveDataForm(event, formID, reDrawDiv).then()})

//Ловим событие формы RECALCULATIONS
document.getElementById("recalcBtn").addEventListener('click', event => {
    let formID = 'recalculations_form';
    let reDrawDiv = 'recalcList';
    saveDataForm(event, formID, reDrawDiv).then()})

//Ловим событие формы PRIVILEGE
document.getElementById("privilegeBtn").addEventListener('click', event => {
    let formID = 'privilege_form';
    let reDrawDiv = 'privilegesList';
    saveDataForm(event, formID, reDrawDiv).then()})

//Ловим событие формы SUBSIDIES
document.getElementById("subsidiesBtn").addEventListener('click', event => {
    let formID = 'subsidies_form';
    let reDrawDiv = '.subsidies_list';
    saveDataForm(event, formID, reDrawDiv).then()})
