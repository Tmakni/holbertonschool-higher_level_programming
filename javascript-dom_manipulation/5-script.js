const trigger = document.querySelector('#update_header');
const header  = document.querySelector('header');

trigger.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
