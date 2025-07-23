document.addEventListener('DOMContentLoaded', function () {
  document.getElementById("btn_translate").addEventListener("click", function () {
    const lang = document.getElementById("language_code").value;

    fetch("https://hellosalut.stefanbohacek.com/?lang=" + lang)
      .then(response => response.json())
      .then(data => {
        document.getElementById("hello").textContent = data.hello;
      })
      .catch(error => {
        console.error('Erreur lors du fetch:', error);
      });
  });
});