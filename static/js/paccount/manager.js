window.onload = function() {

    async function saveDataForm(event, formID) {
        event.preventDefault();
        
        // Парсит данные с формы и возвращает объект -> {'csrf': token, 'body': body}
        function parceFormData (formData) {
            let str = '';
            let token = formData.get("csrfmiddlewaretoken")
            for(let [name, value] of formData) {
                str += `${name}=${value}&`};
            return {'csrf': token, 'body': str.slice(0, -1)}}
        
        // Выводим сообщение в соответствующий Alert bootstrap
        function displayCounterAlert(say, typeAlert, time, target){
            try {
                // Если елемента нет пролетаем дальше без ошибки
                document.querySelector('#successAlert').remove();
            } catch{ }

            // Создаем новый div
            let helper = document.createElement('div');
            let html = `<div class="flex-fill  alert  alert-${typeAlert}  mt-3  mb-5" id="successAlert"><p>${say}</p></div>`;
            helper.innerHTML = html;
            let fff = document.querySelector(`#${formID}`)
            document.querySelector(`#${formID}`).before(helper);

            // Таймер показа сообщения
            // setTimeout(function(){
            //     document.querySelector('#successAlert').remove();
            // }, time);
        };

        const formData = new FormData(document.getElementById(formID));
        const request = parceFormData(formData);
        const response = await fetch(window.location.href, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-CSRFToken': request['csrf']
            },
            body: ''})

        if (response.ok) {
            let say = `Данные успешно приняты!`;
            let time = 15000;
            let typeAlert = `success`;
            displayCounterAlert(say, typeAlert, time, event.target.id);
        } else {
            let say = `Что-то пошло не так! Попробуйте чуть позже!`;
            let time = 15000;
            let typeAlert = `danger`;
            displayCounterAlert(say, typeAlert, time, event.target.id);
        }
    }

    //Ловим событие формы CURRENT
    document.querySelector("#formationPayBtn").addEventListener('click', event => {
        let formID = 'formationPayForm';
        saveDataForm(event, formID).then()});
};
