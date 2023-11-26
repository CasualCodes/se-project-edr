var video = document.getElementById('video');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var start = document.getElementById('start');
var snap = document.getElementById('snap');
var gallery_btn = document.getElementById('gallery');
var assess_lbl = document.getElementById('assess_lbl');
var result_lbl = document.getElementById('result_lbl');
var reassess_btn = document.getElementById('reassess_btn');
var loadFile = function (event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

function showResults() {
    assess_lbl.style.display = 'none';
    start.style.display = 'none';
    gallery_btn.style.display = 'none';
    result_lbl.style.display = "block";
    reassess_btn.style.display = "block";
}

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
    start.addEventListener("click", function () {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
            toggleVisibility('start', 'snap');
            video.srcObject = stream;
            video.play();
            video.style.display = 'block';
        });
    });
}

// Trigger photo take
snap.addEventListener("click", function () {
    toggleVisibility('snap', 'start');
    context.drawImage(video, 0, 0, 640, 480);
    video.style.display = 'none';
    canvas.style.display = 'block';
    // go to results screen
    showResults();
    // assess_lbl.style.display = 'none';
    // start.style.display = 'none';
    // gallery_btn.style.display = 'none';
    // result_lbl.style.display = "block";
    // reassess_btn.style.display = "block";

});