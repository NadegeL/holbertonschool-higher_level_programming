
const updateButton = document.querySelector('#update_header');

const header = document.querySelector('header');

if (updateButton && header) {
    updateButton.addEventListener('click', function() {
        header.textContent = 'New Header!!!';
    });
} else {
    console.log("L'élément #update_header ou l'en-tête n'a pas été trouvé");
}