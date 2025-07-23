document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', function () {
    const ul = document.querySelector('ul.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });
  document.getElementById('remove_item').addEventListener('click', function () {
    const ul = document.querySelector('ul.my_list');
    if (ul.lastElementChild) ul.removeChild(ul.lastElementChild);
  });
  document.getElementById('clear_list').addEventListener('click', function () {
    const ul = document.querySelector('ul.my_list');
    ul.innerHTML = '';
  });
});
