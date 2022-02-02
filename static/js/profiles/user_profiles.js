$(document).ready(function () {
    // Current state structure
    var $currentState = $(".formset_row").clone();

    function setDefaultValue() {
        // Set default value for new forms
        $("input[type='number']").each(function () {
            if (!$(this).val()) {
                $(this).val(0).prop('disabled', false);
            };
        });
        // Renew current state structure
        $currentState = $(".formset_row").clone();
    };

    function itemDelete(row) {
        var quantity_delta = parseInt($(row).find("[type='number']").val());
        $order_total_quantity.text(parseInt($order_total_quantity.text()) - quantity_delta);
        var $price_object = $(row).find("[class^=orderitems]");
        if (!$price_object.length) {
            var item_price = 0;
        } else {
            var item_price = parseFloat($price_object.text());
        };
        $order_total_cost.text(Number(parseFloat($order_total_cost.text()) - quantity_delta * item_price).toFixed(2));
        $currentState = $(".formset_row").clone();
    };

    // Be carefull with class of buttons
    $('.formset_row').formset({
        addText: 'добавить квартиру',
        addCssClass: 'btn btn-outline-primary btn-block',
        deleteText: 'удалить',
        deleteCssClass: 'btn btn-outline-warning',
        prefix: 'appartament_form',
        added: setDefaultValue,
        removed: itemDelete,
        hideLastAddForm: false,
    });
});