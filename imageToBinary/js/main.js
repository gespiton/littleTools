$('.col button').on('click', function () {
    $(this).toggleClass('btn-success');
});

$('button#export').on('click', function () {
    let res = [];
    for (let i = 0; i !== 30; i++) {
        if ($('#' + i).hasClass('btn-success')) {
            res.push(1);
        } else {
            res.push(0);
        }
    }
    console.log(res.toString());
    $('#output').val('{' + res.toString() + '}');
});
