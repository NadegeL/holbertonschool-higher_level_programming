
const redbutton = document.querySelector('#red_header');

const header = document.querySelector('header');

if (redbutton && header) {
    redbutton.addEventListener('click', function() {
        header.style.color = '#FF0000';
    });
} else {
    console.log("#redheader not exist");
}