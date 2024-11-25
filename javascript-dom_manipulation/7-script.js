const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

const movieList = document.querySelector('#list_movies');

fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

/* .then(data=>) : parcourt la liste des films et ajouter chaque titre à la liste HTML*/