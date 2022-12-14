
setTimeout(function() {
    $('#preloader').hide();


    $('.title-app').css('display', 'flex');
    $('.form').css('display', 'flex');
    $('.form-add').css('display', 'flex');
    $('#buy').css('display', 'block');
    $('.right-side').css('display', 'flex');

}, 3000);


// инициализируем списки для упрощения работы с даннымми
window.checked = {}
window.components = ['cpu', 'gpu', 'mather',
    'ram', 'power-block', 'hdd', 'dilivery',
    'mouse', 'keyboard', 'monitor'
]
window.names = {
    'dilivery': "Доставка"
}
window.sub_components = ['mouse', 'keyboard', 'monitor'];


window.price = {}
$('#buy').click(function(e) {


    // получаем чекбоксы:
    // window.checked['cpu'] = $("#cpu-check").is(":checked");
    window.components.forEach(element => {
        if (window.sub_components.includes(element) && $('#sub-components').is(':checked') == false) return;
        window.checked[element] = $(`#${element}-check`).is(":checked");
    });
    // получаем цены: 
    window.components.forEach(element => {

        if (window.checked[element]) {
            if (element == 'dilivery') {
                window.price[element] = 400;
            } else {
                window.price[element] = parseInt($(`#${element}`).val().split(" ")[0])
            }
            if (element == 'ram' || element == 'hdd') {
                window.price[element] = parseInt($(`#${element}`).val().split(" ")[0]) * parseInt($(`#${element}-count`).val())

            }
        }

    });
    window.components.forEach(element => {
        if (element != 'dilivery') {
            window.names[element] = $(`#${element} option:selected`).text()
        }
    })
    var msg = 'Вы заказали:\n'
    var result_price = 0;
    window.components.forEach(element => {
        if (window.checked[element]) {
            msg += `${window.names[element]}: ${window.price[element]}Р \n`
            result_price += window.price[element]
        }

    })
    msg += 'Итоговая стоимость: ' + result_price
    window.msg_box = msg.replace(/(?:\r\n|\r|\n)/g, "<br>");
    if (window.checked["dilivery"] && $("#address").val() != "") {
        window.msg_box += `<br> Адрес доставки: ${$('#address').val()}`
    }
    document.querySelector("#output-p").innerHTML = `${window.msg_box}`
    $('.modal-buy').animate({
        "top": '8%'
    }, 800)
    $('#get-docx').click(function(e) {
        $('#text-docx').val(window.msg_box)
        $('#form-download').submit()
    });

    $('#close-modal').click(function(){
        $('.modal-buy').animate({
            "top": '-120%'
        }, 800)
        document.querySelector("#output-p").innerHTML = ``;
        
    })

});

$('#sub-components').click(function (e) { 
    if($('#sub-components').is(':checked')) {
        
$.ajax({
    url: '/get_sub_components',
    success: function (response) {
        document.querySelector('.sub-component-form').innerHTML = response;
    }
  });
    } else {
        document.querySelector('.sub-component-form').innerHTML = '';
    }
    
});