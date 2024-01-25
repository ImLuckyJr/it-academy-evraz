const titleDOM = document.getElementById('title');
const descriptionDOM = document.getElementById('description');
const buttonAdd = document.getElementById('add');
const listDOM = document.getElementById('list');
const formDOM = document.getElementById('form');

let items = [];

function generateHtml(object) {
    const newDivHTML = `<div class="title">${ object.title }</div><div class="description">${ object.description }</div>`;
    const newDiv = document.createElement('div');
    newDiv.innerHTML = newDivHTML;
    listDOM.appendChild(newDiv);
}

if (titleDOM && descriptionDOM && buttonAdd && listDOM) {
    items = localStorage.getItem('items');
    items = JSON.parse(items) || [];
    
    for (let item of items) {
        generateHtml(item);
    }
    
    buttonAdd.addEventListener('click', function(event) {
        const title = titleDOM.value;
        const description = descriptionDOM.value;
        
        if (!title) {
            alert('Укажите заголовок!');
            return;
        }
        
        if (!description) {
            alert('Укажите описание!');
            return;
        }
        
        const object = { title, description };
        generateHtml(object);
        items.push(object);
        localStorage.setItem('items', JSON.stringify(items));
        
        // titleDOM.value = '';
        // descriptionDOM.value = '';
        formDOM.reset();
    });
}
else {
    console.error('Отсутствуют какие-то поля');
}
