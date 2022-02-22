window.onload = function() {

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


    // =============================
    // ======= MANAGER_LIST ========
    // =============================

    //Ловим событие формы CURRENT
    document.querySelector("#currentCountBtn").addEventListener('click', event => {
        let formID = 'house_count_form';
        let reDrawDiv = '.house-current_list';
        saveDataForm(event, formID, reDrawDiv).then()})

    // //Ловим событие формы RECALCULATIONS
    // document.querySelector("#recalcBtn").addEventListener('click', event => {
    //     let formID = 'recalculations_form';
    //     let reDrawDiv = '.recalc_list';
    //     saveDataForm(event, formID, reDrawDiv).then()})

    // //Ловим событие формы PRIVILEGE
    // document.querySelector("#privilegeBtn").addEventListener('click', event => {
    //     let formID = 'privilege_form';
    //     let reDrawDiv = '.privileges_list';
    //     saveDataForm(event, formID, reDrawDiv).then()})

    // //Ловим событие формы SUBSIDIES
    // document.querySelector("#subsidiesBtn").addEventListener('click', event => {
    //     let formID = 'subsidies_form';
    //     let reDrawDiv = '.subsidies_list';
    //     saveDataForm(event, formID, reDrawDiv).then()})

    // //Ловим событие формы PAYNENTS
    // document.querySelector("#paymentsBtn").addEventListener('click', event => {
    //     let formID = 'payments_form';
    //     let reDrawDiv = '.payments_list';
    //     saveDataForm(event, formID, reDrawDiv).then()})


    // =============================
    // ======== USER_LIST ==========
    // =============================

    // //Ловим событие формы COUNTERFORM
    // document.getElementById('counterBtn').addEventListener('click', event => {
    //     let formID = 'counterForm';
    //     let reDrawDiv = '';  //TODO Добавить на страницу к ЮЗЕРУ таблицу с введенными данными
    //     saveDataForm(event, formID, reDrawDiv).then()})
}
