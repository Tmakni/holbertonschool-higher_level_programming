(async () => {
  const list = document.querySelector('#list_movies');
  try {
    const res   = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const data  = await res.json();
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      list.appendChild(li);
    });
  } catch (err) {
    console.error(err);
    list.innerHTML = '<li>Erreur de chargement 🙁</li>';
  }
})();
