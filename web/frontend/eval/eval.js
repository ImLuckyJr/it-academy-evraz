const answer = document.getElementById('answer');
const input = document.getElementById('input');
const button = document.getElementById('button');
// const body = document.getElementById('body');

if (answer && input && button) {
    button.addEventListener('click', function(event) {
        // console.log(event);
        // console.log(event.target);
        // console.log(event.target.innerText);
        
        console.log(input.value);
        // input.value = '20+20';
        answer.innerText += eval(input.value);
    });
    // body.addEventListener('click', function(event) {
    //     console.log(event);
    //     console.log(event.target);
    //     console.log(event.target.innerText);
    // });
}
else {
    console.error('Нет какого-то поля');
}
