const url = window.location.href
let addBtn = $('#add');
let subtractBtn = $('#subtract');
let multiplyBtn = $('#multiply');
let divideBtn = $('#divide')
let inputA = $('#input_A')[0]
let inputB = $('#input_B')[0]
let result = $('#result')


function add(a, b, oper) {
    let token = $("[name=csrfmiddlewaretoken]").val();
    let urlRequest = url + '/add/'
    switch (oper) {
        case 'add':
            break
        case 'subtract':
            urlRequest = url + '/subtract/';
            break
        case 'multiply':
            urlRequest = url + '/multiply/';
            break
        case 'divide':
            urlRequest = url + '/divide/';
            break
    }
    $.ajax({
        url: urlRequest,
        type: 'POST',
        data: JSON.stringify({
            "A": a,
            "B": b
        }),
        contentType: "application/json",
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", token);
        },
        success: function (data) {
            result[0].style.color = 'green'
            result.text(`Результат: ${data.answer}`)
        },
        error: function (xhr, status, error) {
            result[0].style.color = 'red'
            result.text(`Результат: ${xhr.responseJSON.error}`);
            console.log(xhr);
            console.log(status);
            console.log(error);
        }
    })

}
let test = function (event) {
    event.preventDefault();
    let oper = event.currentTarget.id;
    add(inputA.value, inputB.value, oper)
}

addBtn.on('click', test);
subtractBtn.on('click', test);
multiplyBtn.on('click', test);
divideBtn.on('click', test);