// наши инпуты
let input1 = document.getElementById('inp1');
let input2 = document.getElementById('inp2');

// дивы, где лежат инпуты (их контейнеры)
let divinput1 = document.getElementById('divinp1');
let divinput2 = document.getElementById('divinp2');

// див для вывода результата
let result = document.getElementById('res');

function checkNumber() {
    // удаляем класс из каждого дива, чтобы убрать зеленое выделение (класс higher делает выделение зелёным, можете проверить в css файле)
    divinput1.classList.remove('higher');
    divinput2.classList.remove('higher');
    
    // преобразуем введенное число в виде строки к числу
    let a = +input1.value;
    let b = +input2.value;
    
    // здесь будет храниться ответ по проверке
    let answer = '';
    
    /**
     * Это еще один вид комментариев, позволяющий делать многострочные комментарии.
     * Как указанно в комментарии ниже, вам ниже необходимо написать свой код, своё условие для реализации данной задачи.
     *
     * Чтобы сделать как на гифке выделение зеленым цветом инпута, где указано большее число, необходимо воспользоваться командой:
     * divinput1.classList.add('higher'); // это для первого блока
     * divinput2.classList.add('higher'); // это для второго блока
     *
     * Обратите внимание, отличается только переменная, к которой мы обращаемся (divinput1 или dininput2), которые были созданы в начале файла
     */
    
    // ЗДЕСЬ НЕОБХОДИМО НАПИСАТЬ УСЛОВИЯ (для вас уже готовы переменные a и b, не забудьте)
    
    result.innerText = answer;
}