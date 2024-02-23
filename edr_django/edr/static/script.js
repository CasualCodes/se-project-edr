document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.main_nav_icon').addEventListener('click', function () {
        document.querySelector('nav ul').classList.toggle('active');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.nav_icon').addEventListener('click', function () {
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
    icon.src = lightmodeurl;
    if (assess) assess.src = lightassessurl;
    if (library) library.src = lightlibraryurl;
    if (nav_icon) nav_icon.src = navicon2url;
    if (upload) upload.src = lightuploadurl;
} else {
    icon.src = darkmodeurl;
    if (assess) assess.src = darkassessurl;
    if (library) library.src = darklibraryurl;
    if (nav_icon) nav_icon.src = naviconurl;
    if (upload) upload.src = darkuploadurl;
}

// Toggle theme when the icon is clicked
icon.onclick = function () {
    document.body.classList.toggle("light-theme");
    if (document.body.classList.contains("light-theme")) {
        icon.src = "{% static '' %}LightMode.png";
        if (assess) assess.src = "{% static '' %}LightAssess.jpg";
        if (library) library.src = "{% static '' %}LightLibrary.jpg";
        if (nav_icon) nav_icon.src = "{% static '' %}NavIcon2.png";
        if (upload) upload.src = "{% static '' %}LightUplaod.jpg";
        // Store the theme preference
        localStorage.setItem('theme', 'light-theme');
    } else {
        icon.src = "{% static '' %}DarkMode.png";
        if (assess) assess.src = "{% static '' %}DarkAssess.jpg";
        if (library) library.src = "{% static '' %}DarkLibrary.jpg";
        if (nav_icon) nav_icon.src = "{% static '' %}NavIcon.png";
        if (upload) upload.src = "{% static '' %}DarkUpload.jpg";
        // Store the theme preference
        localStorage.setItem('theme', '');
    }
}

















var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var start = document.getElementById('start');
var snap = document.getElementById('snap');
var gallery_btn = document.getElementById('gallery');
var assess_lbl = document.getElementById('assess_lbl');
// var result_lbl = document.getElementById('result_lbl');
// var reassess_btn = document.getElementById('reassess_btn');
// var gallery_img = document.getElementById('galleryOutput');

var id_imgfile = document.getElementById('id_imgfile'); // choose file field
// id_imgfile.style.display = 'none';
var upload_btn = document.getElementById('upload_btn');

// function showResults() {
//     assess_lbl.style.display = 'none';
//     start.style.display = 'none';
//     snap.style.display = 'none';
//     gallery_btn.style.display = 'none';
//     result_lbl.style.display = "block";
//     reassess_btn.style.display = "block";
// }

// function showAssessScreen() {
//     assess_lbl.style.display = 'block';
//     start.style.display = 'block';
//     snap.style.display = 'none';
//     gallery_btn.style.display = 'block';

//     canvas.style.display = "none";
//     gallery_img.style.display = "none";
//     result_lbl.style.display = "none";
//     reassess_btn.style.display = "none";
// }

// var loadFile = function (event) {
//     gallery_img.src = URL.createObjectURL(event.target.files[0]);
//     gallery_img.style.maxWidth='45%';
//     gallery_img.style.maxHeight='45%';
//     gallery_img.style.margin='auto';
//     gallery_img.style.display = 'block';
//     showResults();
// };

id_imgfile.addEventListener('change', function (event) {
    upload_btn.click();

    // var file = id_imgfile.files[0];
    // var formData = new FormData();
    // formData.append('file', file);

    // fetch('/media/images', { // replace with your upload endpoint
    //     method: 'POST',
    //     body: formData
    // })
    // .then(response => response.json())
    // .then(success => {
    //     // redirects after the server responds that the file upload is complete
    //     document.location.href='/edr/results/' + file.name;
    // })
    // .catch(error => console.log(error));
});


function toggleVisibility(source, target) {
    var target_btn = document.getElementById(target);
    var source_btn = document.getElementById(source);
    if (target_btn.style.display === "none") {
        target_btn.style.display = "block";
        source_btn.style.display = "none";
    } else {
        target_btn.style.display = "none";
        source_btn.style.display = "block";
    }
}

// Get access to the camera!
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    var stream;
    start.addEventListener("click", function () {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function (mediaStream) {
            toggleVisibility('start', 'snap');
            video.srcObject = mediaStream;
            video.play();
            video.style.display = 'block';
            gallery_btn.style.display = 'none';
            stream = mediaStream; // keep a reference to the stream
        });
    });
}

// Trigger photo take
snap.addEventListener("click", function () {
    toggleVisibility('snap', 'start');
    context.drawImage(video, 0, 0, 640, 480);
    video.style.display = 'none';
    canvas.style.display = 'block';
    if (stream) {
        stream.getTracks().forEach(function (track) {
            track.stop();
        });
    }
    // go to results screen
    // showResults();
});

// reassess_btn.addEventListener("click", function () {
//     showAssessScreen();
// });