function changeText() {
    let newText = prompt('Введите новый текст');
    let div = document.getElementById('change');
    div.innerText = newText;
}