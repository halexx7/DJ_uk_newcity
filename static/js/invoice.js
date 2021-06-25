//Конвертим дату в формат - Январь 2021
function convertDate(item) {
    let date = new Date(Date.parse(item))

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
    }
}

// Добавим верхнюю часть Шапки
$('.header__top').append(
    `<p class="header__top--payer"> За <span style="font-weight: bold; font-size: 1.4rem;">${convertDate(period)}</span>Плательщик: <span class="text__sum">${header.payer}</span> </p>
    <p> Адрес: ${header.address}</p>
    <p> Площащь: ${header.sq_appart} м2 Количество проживающих: ${header.num_living}</p>
    <p> Управляющая компания: ${header.name_uk.name}, ${header.name_uk.address}, ${header.name_uk.phone}</p>`,
);

// Добавим среднюю часть Шапки
$('.header__center').append(
    `<p> получатель платежа: ${header.name_uk.name} р/с ${header.requisites.check_acc} ИНН ${header.requisites.inn} ${header.requisites.bank} БИК ${header.requisites.bik} к/с ${header.requisites.corr_acc}</p>
     <p> Адрес сайта: <span class="text__period"> ${header.name_uk.web} </span></p>
     <p> Лицевой счет: <span class="text__sum">${header.personal_account}  </span> сумма к оплате: <span class="text__sum" id="headerTotal"> </span> р.</p>`
);


// Добавляет таблицу с итогами
$('.header__bottom').append('<table style="width: 606px;"></table>');

$('.header__bottom > table').append(
    `<tr>
        <th>Задолженность/Аванс</th>
        <th>Начислено за месяц</th>
        <th>Перерасчеты</th>
        <th>Субсидии</th>
        <th>Льготы</th>
        <th>Оплачено в тек.месяце</th>
        <th>Итого к оплате</th>
    </tr>`
);

$('.header__bottom > table').append(
    `<tr class="text__center">
        <td id="subHeaderStatus">0.00</td>
        <td id="subHeaderPre">5601,08</td>
        <td id="subHeaderRecalc">-313,66</td>
        <td id="subHeaderSubsid">414,56</td>
        <td id="subHeaderPrivil">414,56</td>
        <td>5480,86</td>
        <td id='subHeaderTotal'></td>
    </tr>`
);

// добавим Таблицу расчетов что - за что
$('.body__content').append('<table></table>');

// Шапка таблицы расчетов
$('.body__content > table').append(
    `<tr>
        <th>Виды услуг</th>
        <th>Ед.изм.</th>
        <th>Норматив</th>
        <th>Объем</th>
        <th>Тариф</th>
        <th>Начисленно<br>руб.</th>
        <th>коэф-т</th>
        <th>Субсидии<br>руб.</th>
        <th>Льготы<br>руб.</th>
        <th>Перерасчет<br>руб.</th>
        <th>Итого<br>за расчетный<br>период</th>
    </tr>`
);

// Пройдем циклом по всем элементам массива и сгенерируем строки таблицы
function drawingTable (object) {
    let total = Number(), totalPre = Number(), totalSubs = Number(), totalPrivi = Number(), totalRecal = Number();
    object.forEach(function (item, i, arr) {
        total += Number(item.total)
        totalPre += Number(item.pre_total);ы
        totalSubs += Number(item.subsidies);
        totalPrivi += Number(item.privileges);
        totalRecal += Number(item.recalculation);

        $('.body__content > table').append(
            `<tr>
            <td class="pad__table">${item.service}</td>
            <td class="text__center  pad__table">${item.unit}</td>
            <td class="text__right  pad__table">${(item.standart > 0) ? item.standart: ''}</td>
            <td class="text__right  pad__table">${item.volume}</td>
            <td class="text__right  pad__table">${item.rate}</td>
            <td class="text__right  pad__table">${Number(item.accured).toFixed(3)}</td>
            <td class="text__right  pad__table">${item.coefficient}</td>
            <td class="text__right  pad__table">${(item.subsidies > 0) ? parseFloat(item.subsidies).toFixed(2): ''}</td>
            <td class="text__right  pad__table">${(item.privileges > 0) ? parseFloat(item.privileges).toFixed(2): ''}</td>
            <td class="text__right  pad__table">${(item.recalculation != 0) ? item.recalculation: ''}</td>
            <td class="text__right  pad__table">${parseFloat(item.total).toFixed(2)}</td>
        </tr>`
        );
    });
    $('#subHeaderRecalc').text((totalRecal).toFixed(2));
    $('#subHeaderSubsid').text((totalSubs).toFixed(2));
    $('#subHeaderPrivil').text((totalPrivi).toFixed(2));
    $('#subHeaderPre').text((totalPre).toFixed(2));
    return [total, totalPre];
}

let total_const = drawingTable(constant);
let total_variable = drawingTable(variable);

//Итого
let total = Number();
total = (total_const[0] + total_variable[0]).toFixed(2);
totalPre = (total_const[1] + total_variable[1]).toFixed(2);

$('#headerTotal').text((status).toFixed(2));

$('#subHeaderPre').text(totalPre);
$('#subHeaderStatus').text((status).toFixed(2));
$('#subHeaderTotal').text((status).toFixed(2));
$('.body__content > table').append(
    `<tr class="table__bold">
        <td colspan="10" style="font-weight: bold;">Итого за расчетный период: </td>
        <td class="text__right  pad__table">${total}</td>
    </tr>`
);


//Слушаем кнопку Печать
$('#invoice-print').on('click', (function(){
    print();
}));

//Слушаем кнопку Сохранить PDF
$('#invoice-pdf').on('click', (function() {
    //Сохраняем в ПДФ
    var pdf = new jsPDF('p', 'pt', 'a4');
    var pdfContainer = document.querySelector('.container');

    //Конвертим в JPEG и сохраняем в PDF
    //Опция scale - задает масштаб относительно разрешения устройства,
    //используем для увеличения разшения pdf
    html2canvas(pdfContainer, {background: "white", scale: 4}).then(function(canvas) {
        pdf.addImage(canvas, "jpeg", 20, 20, 557, 0);
        pdf.save('TEST.pdf');
    });
}));