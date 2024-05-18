document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.main_nav_icon').addEventListener('click', function() {
        document.querySelector('nav ul').classList.toggle('active');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.nav_icon').addEventListener('click', function() {
        document.querySelector('nav ul').classList.toggle('active');
    });
});

// Check if the user has a theme preference stored
var currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    document.body.classList.add(currentTheme);
}

var icon = document.getElementById("theme");
var nav_icon = document.querySelector(".main_nav_icon");
var assess = document.getElementById("assess-image");
var library = document.getElementById("library-image");
var upload = document.getElementById("upload-image");

// Apply the theme from the stored preference
if (document.body.classList.contains("light-theme")) {
    icon.src = "img/LightMode.png";
    if (assess) assess.src = "img/LightAssess.jpg";
    if (library) library.src = "img/LightLibrary.jpg";
    if (nav_icon) nav_icon.src = "img/NavIcon2.png";
    if (upload) upload.src = "img/LightUplaod.jpg";
} else {
    icon.src = "img/DarkMode.png";
    if (assess) assess.src = "img/DarkAssess.jpg";
    if (library) library.src = "img/DarkLibrary.jpg";
    if (nav_icon) nav_icon.src = "img/NavIcon.png";
    if (upload) upload.src = "img/DarkUpload.jpg";
}

// Toggle theme when the icon is clicked
icon.onclick = function () {
    document.body.classList.toggle("light-theme");
    if (document.body.classList.contains("light-theme")) {
        icon.src = "img/LightMode.png";
        if (assess) assess.src = "img/LightAssess.jpg";
        if (library) library.src = "img/LightLibrary.jpg";
        if (nav_icon) nav_icon.src = "img/NavIcon2.png";
        if (upload) upload.src = "img/LightUplaod.jpg";
        // Store the theme preference
        localStorage.setItem('theme', 'light-theme');
    } else {
        icon.src = "img/DarkMode.png";
        if (assess) assess.src = "img/DarkAssess.jpg";
        if (library) library.src = "img/DarkLibrary.jpg";
        if (nav_icon) nav_icon.src = "img/NavIcon.png";
        if (upload) upload.src = "img/DarkUpload.jpg";
        // Store the theme preference
        localStorage.setItem('theme', '');
    }
}







