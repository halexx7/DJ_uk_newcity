//Получатель
var pay = [
    {
        value: "взносы на капитальный ремонт",
        um: "m2",
        standard: "1.3",
        volume: "1.4",
        pricing_plans: "1.5",
        accrued: "1.6",
        coefficient: "1.7",
        subsidies: "1.8",
        recalculations: "1.9",
        total: "1.10"
    }
];

//Конвертим дату в формат - Январь 2021
function convertDate(item) {
    let date = new Date(Date.parse(item))

    switch(date.getMonth()){
        case 0:
            return(` Январь ${date.getFullYear()} `);
            break;
        case 1:
            return(` Февраль ${date.getFullYear()} `);
            break;
        case 2:
            return(` Март ${date.getFullYear()} `);
            break;
        case 3:
            return(` Апрель ${date.getFullYear()} `);
            break;
        case 4:
            return(` Май ${date.getFullYear()} `);
            break;
        case 5:
            return(` Июнь ${date.getFullYear()} `);
            break;
        case 6:
            return(` Июль ${date.getFullYear()} `);
            break;
        case 7:
            return(` Август ${date.getFullYear()} `);
            break;
        case 8:
            return(` Сентябрь ${date.getFullYear()} `);
            break;
        case 9:
            return(` Октябрь ${date.getFullYear()} `);
            break;
        case 10:
            return(` Ноябрь ${date.getFullYear()} `);
            break;
        case 11:
            return(` Декабрь ${date.getFullYear()} `);
            break;
    }
}

let variable_pay = []
//Парсим объект
Object.values(variable).forEach(value => {
    variable_pay.push(value.fields);
  });


// Добавим верхнюю часть Шапки
$('.header__top').append(
    `<p class="header__top--payer"> За <span style="font-weight: bold; font-size: 1.6rem;">${convertDate(variable_pay[0].period)}</span>Плательщик: ${user.name} </p>
    <p> Адрес: ${street.street}, д.${house.number}</p>
    <p> Площащь: ${appartaments.sq_appart} м2 Количество проживающих: ${appartaments.num_owner}</p>
    <p> Управляющая компания: ${uk.name}, ${uk.requisites}</p>`,
);

// Добавим среднюю часть Шапки
$('.header__center').append(
    `<p> получатель платежа: ${uk.name}, ${uk.requisites}  </p>
     <p> Адрес сайта: <span class="text__period"> ${uk.web_addr} </span></p>
     <p> лицевой счет: ${user.personal_account} сумма к оплате: <span class="text__sum"> 4872,86 р.</span></p>`
);

$('.header__bottom').append('<table style="width: 606px;"></table>');

$('.header__bottom > table').append(
    `<tr>
        <th>Задолженность/Аванс</th>
        <th>Начислено за месяц</th>
        <th>Перерасчеты</th><th>Субсидии**</th>
        <th>Оплачено в тек.месяце</th>
        <th>Итого к оплате</th>
    </tr>`
);

$('.header__bottom > table').append(
    `<tr class="text__center">
        <td>5480,86</td>
        <td>5601,08</td>
        <td>-313,66</td>
        <td>414,56</td>
        <td>5480,86</td>
        <td>4872,86</td>
    </tr>`
);


// добавим Таблицу расчетов что - за что
$('.body__content').append('<table></table>');

// добавим шапку
$('.body__content > table').append(
    `<tr>
        <th>Виды услуг</th>
        <th>Ед.изм.</th>
        <th>Норматив</th>
        <th>Объем</th>
        <th>Тариф</th>
        <th>Начисленно<br>руб.</th>
        <th>коэф-т</th>
        <th>Субсидии<br>%</th>
        <th>Льготы<br>%</th>
        <th>Перерасчет<br>руб.</th>
        <th>Итого<br>за расчетный<br>период</th>
    </tr>`
);

console.log(constant);
console.log(variable_pay);

// Пройдем циклом по всем элементам массива и сгенерируем строки таблицы

function drawingTable (object) {
    let total = Number();
    let num = Number();
    object.forEach(function (item, i, arr) {
        num = Number(parseFloat(item.accured).toFixed(3));
        total += num;
        $('.body__content > table').append(
            `<tr>
            <td class="pad__table">${item.service}</td>
            <td class="text__center  pad__table">${item.unit}</td>
            <td class="text__right  pad__table">${(item.standart > 0) ? item.standart: ''}</td>
            <td class="text__right  pad__table">${item.volume}</td>
            <td class="text__right  pad__table">${item.rate}</td>
            <td class="text__right  pad__table">${Number(item.accured).toFixed(3)}</td>
            <td class="text__right  pad__table">${item.coefficient}</td>
            <td class="text__right  pad__table">${(item.subsidies > 0) ? item.subsidies: ''}</td>
            <td class="text__right  pad__table">${(item.privileges > 0) ? item.privileges: ''}</td>
            <td class="text__right  pad__table">${(item.recalculations > 0) ? item.recalculations: ''}</td>
            <td class="text__right  pad__table">${item.total}</td>
        </tr>`
        );
    });
    return total;
}

let total_const = drawingTable(constant);
console.log(total_const);
let tatal_variable = drawingTable(variable_pay);
console.log(tatal_variable);

//Итого
$('.body__content > table').append(
    `<tr class="table__bold">
        <td colspan="10" style="font-weight: bold;">Итого за расчетный период: </td>
        <td class="text__right  pad__table">${(total_const + tatal_variable).toFixed(2)}</td>
    </tr>`
);


//Слушаем кнопку Печать
$('#invoice-print').on('click', (function(){
    print();
}));

//Слушаем кнопку Созранить PDF
$('#invoice-pdf').on('click', (function() {
    //Сохраняем в ПДФ
    var pdf = new jsPDF('p', 'pt', 'a4');
    var pdfContainer = document.querySelector('.content');

    //Конвертим в JPEG и сохраняем в PDF
    //Опция scale - задает масштаб относительно разрешения устройства,
    //используем для увеличения разшения pdf
    html2canvas(pdfContainer, {background: "white", scale: 4}).then(function(canvas) {
        pdf.addImage(canvas, "jpeg", 20, 20, 557, 0);
        pdf.save('TEST.pdf');
    });
}));