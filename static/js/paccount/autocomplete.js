async function saveDataForm(event, formID, reDrawDiv) {
    event.preventDefault();
    
    // Парсит данные с формы и возвращает объект -> {'csrf': token, 'body': body}
    function parceFormData (formData) {
        let str = '';
        let token = formData.get("csrfmiddlewaretoken")
        for(let [name, value] of formData) {
            str += `${name}=${value}&`};
        return {'csrf': token, 'body': str.slice(0, -1)}}
    
    // Очищаем инпуты
    function clearInput(arr) {
        arr.forEach(element => {
            element.value = '';
        });};
    
    // Выводим сообщение в соответствующий Alert bootstrap
    function displayCounterAlert(say, typeAlert, time, target){
        try {
            // Если елемента нет пролетаем дальше без ошибки
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
    const request = parceFormData(formData);
    const response = await fetch(window.location.href, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-CSRFToken': request['csrf']
        },
        body: request['body']})

    if (response.ok) {
        let json = await response.json();
        let say = `Данные успешно приняты!`;
        let time = 15000;
        let typeAlert = `success`;
        displayCounterAlert(say, typeAlert, time, event.target.id);
        document.querySelector(reDrawDiv).innerHTML = json.instance;
    } else {
        let say = `Что-то пошло не так! Попробуйте чуть позже!`;
        let time = 15000;
        let typeAlert = `danger`;
        displayCounterAlert(say, typeAlert, time, event.target.id);
    }
}

async function autocomplete(inp) {
    var currentFocus;
    let request = {
        url: `${window.location.href}autocomplete/`,
        csrf: getCookieCSRF(),
    }

    async function getAjaxRequest(body) {
        const response = await fetch(request.url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRFToken': request['csrf']
            },
            body: JSON.stringify(body)})
        
        if (response.ok) {
            let json = await response.json();
            return json;
        }
    };

    inp.addEventListener("input", async function(e) {
        let a, b, i, body, arr, val = this.value;
        closeAllLists();
        if (!val || (val.length < 3)) { return false;}
        currentFocus = -1;

        body = {type: this.id, value: this.value}
        responce = await getAjaxRequest(body);
        arr = Object.keys(responce['value']);

        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");

        this.parentNode.appendChild(a);
        for (i = 0; i < arr.length; i++) {
          if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
            b = document.createElement("DIV");
            b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
            b.innerHTML += arr[i].substr(val.length);
            b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";

                b.addEventListener("click", function(e) {
                inp.value = this.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            a.appendChild(b);
          }
        }
    });

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

    function closeAllLists(elmnt) {
      var x = document.getElementsByClassName("autocomplete-items");
      for (var i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inp) {
        x[i].parentNode.removeChild(x[i]);
      }
    }
  }

  document.addEventListener("click", function (e) {
      closeAllLists(e.target);
  });
  }