
const addButton = document.querySelector('#add_item');

const myList = document.querySelector('ul.my_list');

if (addButton && myList) {
    addButton.addEventListener('click', function() {
        const newItem = document.createElement('li');
        
        newItem.textContent = 'Item';
        
        myList.appendChild(newItem);
    });
} else {
    console.log("#add_item or ul.my_list don't exist");
}