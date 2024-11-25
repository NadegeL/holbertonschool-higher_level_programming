document.addEventListener('DOMContentLoaded', function() {
    const helloElement = document.getElementById('hello');
    
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        if (!response.ok) {
          throw new Error('Erreur réseau');
        }
        return response.json();
      })
      .then(data => {
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Erreur:', error);
        helloElement.textContent = 'Erreur de chargement';
      });
  });