const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('#hello');
  fetch(url)
    .then(res => res.json())
    .then(data => {
      container.textContent = data.hello;
    })
    .catch(err => {
      console.error('Fetch error:', err);
      container.textContent = 'Erreur de chargement 🙁';
    });
});
