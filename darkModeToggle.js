// darkModeToggle.js

document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const colorThemeDarkModeToggle = document.getElementById('color-theme-dark-mode-toggle');

    colorThemeDarkModeToggle.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
    });
});
