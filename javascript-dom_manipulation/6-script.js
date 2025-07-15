const output = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(res => res.json())
  .then(data => output.textContent = data.name)
  .catch(err => {
    console.error(err);
    output.textContent = 'Erreur de chargement';
  });
