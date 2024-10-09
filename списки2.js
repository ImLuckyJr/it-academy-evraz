let button = document.getElementById('add');

if (button) {
    button.addEventListener('click', function(event) {
        let elem = event.target;
        elem.innerText = `<div>че <b>с</b> <i>деньгами?</i></div>`;
    });
}
else {
    console.error('Нет кнопки');
}
