const calc = document.querySelector('.calc');
const result = document.querySelector('#result')

calc.addEventListener('click', function(event) {
    if (!event.target.classList.contains('calc__btn')) return;
    
    const value = event.target.innerText;
    
    switch(value) {
        case 'C':
            result.innerText = '';
            break;
        case '=':
            result.innerText = eval(result.innerText).toFixed(2);
            break;
        default:
            result.innerText += value;
    }
})
