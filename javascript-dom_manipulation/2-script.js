const redButton = document.querySelector('#red_header');
const header    = document.querySelector('header');

redButton.addEventListener('click', () => {
  header.classList.add('red');
});
