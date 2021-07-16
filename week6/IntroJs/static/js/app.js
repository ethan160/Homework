// var li1 = document.getElementById('listOne')
// console.log(li1.innerText)

// Event
// var titleELement = document.getElementById("title");
// titleELement.addEventListener('mouseenter', () => alert('It works'));

var addBtn = document.getElementById('addBtn');
var delBtn = document.getElementById('delBtn');
var todoItemField = document.getElementById('todo-item');
var ul = document.getElementById('todo-list-container');
// console.log(todoItemField.value)

function deleteList() {

}

// class in HTML
function changeActiveClass() {
    this.classList.toggle('active');
}

// change the text color upon click
function completedItem() {
    this.classList.add('text-muted');
}

addBtn.addEventListener('click', (e) => {
    e.preventDefault();
    // create new element
    var li = document.createElement('li');

    // Set the innerHTML to what's inside the input field
    li.innerHTML = todoItemField.value;

    // Add the classes
    li.classList.add('list-group-item');

    // Add it into the ul
    ul.appendChild(li);

    // Add the toggle event listener
    li.addEventListener("mouseover", changeActiveClass);
    li.addEventListener("mouseleave", changeActiveClass);

    // OR 
    // ul.innerHTML += `<li onmouseover="changeActiveClass(this)" onmouseleave="changeActiveClass(this)" class="list-group-item">${todoItemField.value}</li>`

    // I added this to gray out text on click of list item (complete)
    li.addEventListener("click", completedItem);

    todoItemField.value = '';
    // console.log(todoItemField.value)
})

// clear all of items upon click 
delBtn.addEventListener('click', (e) => {
    ul.empty('todo-list-container');
})

