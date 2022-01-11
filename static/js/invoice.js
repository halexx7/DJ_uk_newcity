class Invoice {
    constructor() {
        this.header;
        this.period;
        this.constant;
        this.variable;
        this.amount;
        this.pre_amount;
        this.status;
        this.paid;

        this.total;
    };

    // Конвертируем дату в формат - Январь 2021
    convertDate(srcDate) {
        let date = new Date(Date.parse(srcDate))

        switch(date.getMonth()){
            case 0:
                return(` Январь ${date.getFullYear()} `);
            case 1:
                return(` Февраль ${date.getFullYear()} `);
            case 2:
                return(` Март ${date.getFullYear()} `);
            case 3:
                return(` Апрель ${date.getFullYear()} `);
            case 4:
                return(` Май ${date.getFullYear()} `);
            case 5:
                return(` Июнь ${date.getFullYear()} `);
            case 6:
                return(` Июль ${date.getFullYear()} `);
            case 7:
                return(` Август ${date.getFullYear()} `);
            case 8:
                return(` Сентябрь ${date.getFullYear()} `);
            case 9:
                return(` Октябрь ${date.getFullYear()} `);
            case 10:
                return(` Ноябрь ${date.getFullYear()} `);
            case 11:
                return(` Декабрь ${date.getFullYear()} `);
        };
    };

    // Парсим данные
    parseData(paid, orders, status) {
        this.header = JSON.parse(orders[0].fields.header_data);
        this.period = orders[0].fields.period;
        this.constant = JSON.parse(orders[0].fields.constant_data);
        this.variable = JSON.parse(orders[0].fields.variable_data);
        this.amount = JSON.parse(orders[0].fields.amount);
        this.pre_amount = JSON.parse(orders[0].fields.pre_amount);
        this.status = JSON.parse(status[0].fields.amount);
        this.paid = paid;
    };
    
    // Добавляет верхнюю часть Шапки
    drawingTopHeader() {
        return `<p class="header__top--payer">
                 За <span style="font-weight: bold; font-size: 1.4rem;">${this.convertDate(this.period)}</span>
                 Плательщик: <span class="text__sum">${this.header.payer}</span> </p>
                <p> Адрес: ${this.header.address}</p>
                <p> Площащь: ${this.header.sq_appart} м2 Количество проживающих: ${this.header.num_living}</p>
                <p> Управляющая компания: ${this.header.name_uk.name}, ${this.header.name_uk.address}, ${this.header.name_uk.phone}</p>`;
    };

    // Добавляет среднюю часть Шапки
    drawingMiddleHeaer() {
        return `<p> получатель платежа: ${this.header.name_uk.name} 
                р/с ${this.header.requisites.check_acc} 
                ИНН ${this.header.requisites.inn} ${this.header.requisites.bank} 
                БИК ${this.header.requisites.bik} 
                к/с ${this.header.requisites.corr_acc}</p>
                <p> Адрес сайта: <span class="text__period"> ${this.header.name_uk.web} </span></p>
                <p> Лицевой счет: <span class="text__sum">${this.header.personal_account}  </span> 
                    сумма к оплате: <span class="text__sum" id="headerTotal"> </span> р.</p>`;
    };

    // Добавляет таблицу с итогами
    drawingTableHeaer() {
        return `<table style="width: 606px;">
                <tr><th>Задолженность/Аванс</th><th>Начислено за месяц</th><th>Перерасчеты</th>
                    <th>Субсидии</th><th>Льготы</th><th>Оплачено в тек.месяце</th><th>Итого к оплате</th>
                </tr>
                <tr class="text__center">
                    <td id="subHeaderStatus">0.00</td><td id="subHeaderPre">0.00</td>
                    <td id="subHeaderRecalc">0.00</td><td id="subHeaderSubsid">0.00</td>
                    <td id="subHeaderPrivil">0.00</td><td id="subHeaderPaid">0.00</td>
                    <td id="subHeaderTotal">0.00</td>
                </tr>
                </table>`;
    };

    // Добавляем шапку таблицы с расчетами услуг
    drawingContentHeader() {
        return `<tr>
                    <th>Виды услуг</th><th>Ед.изм.</th><th>Норматив</th><th>Объем</th><th>Тариф</th>
                    <th>Начисленно<br>руб.</th><th>коэф-т</th><th>Субсидии<br>руб.</th><th>Льготы<br>руб.</th>
                    <th>Перерасчет<br>руб.</th><th>Итого<br>за расчетный<br>период</th>
                </tr>`;
    };

    // Рисуем строку таблицы услуг
    drawingRowTable(item) {
        return `<tr>
                    <td class="pad__table">${item.service}</td>
                    <td class="text__center  pad__table">${item.unit}</td>
                    <td class="text__right  pad__table">${(item.standart > 0) ? item.standart: ''}</td>
                    <td class="text__right  pad__table">${(item.volume > 0) ? parseFloat(item.volume).toFixed(3): ''}</td>
                    <td class="text__right  pad__table">${item.rate}</td>
                    <td class="text__right  pad__table">${Number(item.accured).toFixed(3)}</td>
                    <td class="text__right  pad__table">${item.coefficient}</td>
                    <td class="text__right  pad__table">${(item.subsidies > 0) ? parseFloat(item.subsidies).toFixed(2): ''}</td>
                    <td class="text__right  pad__table">${(item.privileges > 0) ? parseFloat(item.privileges).toFixed(2): ''}</td>
                    <td class="text__right  pad__table">${(item.recalculation != 0) ? item.recalculation: ''}</td>
                    <td class="text__right  pad__table">${parseFloat(item.total).toFixed(2)}</td>
                </tr>`;
    };

    // Пройдем циклом по всем элементам массива и сгенерируем строки таблицы
    drawingContentBody(object) {
        let listHtml = '';
        object.forEach(item => {
            listHtml += this.drawingRowTable(item);
        });
        return listHtml;
    };

    sumTotal(object) {
        let calculate = {
            total: 0,
            totalPre: 0,
            totalSubs: 0,
            totalPrivi: 0,
            totalRecal: 0
        }
        object.forEach(item => {
            calculate.total += Number(item.total),
            calculate.totalPre += Number(item.pre_total);
            calculate.totalSubs += Number(item.subsidies);
            calculate.totalPrivi += Number(item.privileges);
            calculate.totalRecal += Number(item.recalculation);
        });
        return calculate;
    };

    // Возвращает строку ИТОГО
    drawingContentTotal(total) {
        return `<tr class="table__bold">
                    <td colspan="10" style="font-weight: bold;">Итого за расчетный период: </td>
                    <td class="text__right  pad__table">${total}</td>
                </tr>`;
    };

    //Обновляет данные в суб-хедере и Хедере
    updateHeaderData(constant, variable) {
        document.querySelector('#subHeaderRecalc').textContent = (constant.totalRecal + variable.totalRecal).toFixed(2);
        document.querySelector('#subHeaderSubsid').textContent = (constant.totalSubs + variable.totalSubs).toFixed(2);
        document.querySelector('#subHeaderPrivil').textContent = (constant.totalPrivi + variable.totalPrivi).toFixed(2);
        document.querySelector('#subHeaderPre').textContent = (constant.totalPre + variable.totalPre).toFixed(2);
        document.querySelector('#subHeaderPaid').textContent = (this.paid).toFixed(2);
        document.querySelector('#subHeaderStatus').textContent = (this.status).toFixed(2);
        document.querySelector('#subHeaderTotal').textContent = (this.status).toFixed(2);

        document.querySelector('#headerTotal').textContent = (this.status).toFixed(2);
    };

    // Отрисовывает полностью платежку
    render() {
        document.querySelector('.header__top').innerHTML = this.drawingTopHeader();
        document.querySelector('.header__center').innerHTML = this.drawingMiddleHeaer();
        document.querySelector('.header__bottom').innerHTML = this.drawingTableHeaer();

        const bodyContent = document.querySelector('.body__content');
        let elContent = document.createElement('table');

        elContent.insertAdjacentHTML('beforeend', this.drawingContentHeader());
        elContent.insertAdjacentHTML('beforeend', this.drawingContentBody(this.constant));
        elContent.insertAdjacentHTML('beforeend', this.drawingContentBody(this.variable));

        let calcConstant = this.sumTotal(this.constant);
        let calcVariable = this.sumTotal(this.variable);
        let total = (calcConstant.total + calcVariable.total);

        elContent.insertAdjacentHTML('beforeend', this.drawingContentTotal(total.toFixed(2)));
        bodyContent.appendChild(elContent);

        this.updateHeaderData(calcConstant, calcVariable);
    };
};


let invoice = new Invoice();
invoice.parseData(paid, orders, stats);
invoice.render();


//Слушаем кнопку Печать
const $invoicePrint = document.getElementById('invoice-print');
$invoicePrint.addEventListener('click', () => {
    print();
}, false);

//Слушаем кнопку Сохранить PDF
const $invoicePdf = document.getElementById('invoice-pdf');
$invoicePdf.addEventListener('click', () => {
    //Сохраняем в ПДФ
    var pdf = new jsPDF('p', 'pt', 'a4');
    var pdfContainer = document.querySelector('.container');

    //Конвертим в JPEG и сохраняем в PDF
    //Опция scale - задает масштаб относительно разрешения устройства,
    //используем для увеличения разшения pdf
    html2canvas(pdfContainer, {background: "white", scale: 4}).then(function(canvas) {
        pdf.addImage(canvas, "jpeg", 20, 20, 557, 0);
        pdf.save(`invoice_${period}.pdf`);
    });
}, false);
