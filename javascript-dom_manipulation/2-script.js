//id "red_header"
const redbutton = document.querySelector('#red_header');

const header = document.querySelector('header');

if (redbutton && header) {
    redbutton.addEventListener('click', function() {
        header.classList.add('red');
        header.style.color = '#FF0000';
    });
} else {
    console.log("L'élément #red_header ou l'en-tête n'a pas été trouvé");
}