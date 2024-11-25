// id "toggle_header"
const toggleButton = document.querySelector('#toggle_header');

const header = document.querySelector('header');

if (toggleButton && header) {
    toggleButton.addEventListener('click', function() {
        if (header.classList.contains('red')) {
            header.classList.replace('red', 'green');
        } else if (header.classList.contains('green')) {
            // Si la classe est 'green', la remplacer par 'red'
            header.classList.replace('green', 'red');
        } else {
            // Si aucune classe n'est présente, ajouter 'red' par défaut
            header.classList.add('red');
        }
    });
} else {
    console.log("L'élément #toggle_header ou l'en-tête n'a pas été trouvé");
}