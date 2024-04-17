if (inLibrary) {
    //LIBRARY
    function conditionClick() {
        document.querySelectorAll('.condition').forEach(item => {
            item.addEventListener('click', event => {
                document.querySelectorAll('.condition').forEach(condition => {
                    condition.classList.remove('selected');
                });
                event.target.classList.add('selected');
                displayInfo(event);
                document.querySelector('.xbutton').style.display = 'block';

                document.querySelector('#info .info-h1').style.display = 'block';
                document.querySelector('#info .eye-info').style.display = 'block';
            });
        });
    }

    if (window.matchMedia("(max-width: 768px)").matches) {
        document.querySelector('.xbutton').style.display = 'none';
        conditionClick();
    } else {
        conditionClick();
    }

    document.querySelector('.xbutton').addEventListener('click', function () {
        if (window.matchMedia("(max-width: 768px)").matches) {
            document.querySelector('.right').style.display = 'none';
            document.querySelector('.xbutton').style.display = 'none';
        }
    });

    window.addEventListener('resize', function () {
        if (window.matchMedia("(min-width: 768px)").matches) {
            document.querySelector('.right').style.display = 'block';
        }
    });

    function displayInfo(event) {
        var eyeCondition = event.target.getAttribute('data-info');
        var eyeInfo = getEyeInfo(eyeCondition);

        var infoClass = 'eye-info';
        if (eyeInfo.name === 'Unknown') {
            infoClass = 'image-info';
            document.getElementById('info').style.backgroundColor = 'transparent';
            document.getElementById('info').style.overflowY = 'hidden';
        } else {
            document.getElementById('info').style.backgroundColor = 'var(--Tertiary)';
            document.getElementById('info').style.overflowY = 'auto';
        }

        function generateContent(content) {
            if (Array.isArray(content)) {
                return '<ul class="info-ul">' + content.map(item => `<li>${item}</li>`).join('') + '</ul>';
            } else {
                return `<p class="info-p">${content}</p>`;
            }
        }

        var infoHTML = `
    <h1 class="info-h1">${eyeInfo.name}</h1>
    <div class="${infoClass}">
        ${generateContent(eyeInfo.details)}
        <p class="info-h2">CAUSES</p>
        ${generateContent(eyeInfo.cause)}
        ${eyeInfo.symptoms ? `<p class="info-h2">SYMPTOMS</p>${generateContent(eyeInfo.symptoms)}` : ''}
        ${eyeInfo.treatments ? `<p class="info-h2">TREATMENTS</p>${generateContent(eyeInfo.treatments)}` : ''}
        ${eyeInfo.recommendations ? `<p class="info-h2">RECOMMENDATIONS</p>${generateContent(eyeInfo.recommendations)}` : ''}
    </div>`;

        document.getElementById('info').innerHTML = infoHTML;
        document.querySelector('.right').style.display = 'block';
    }

    function getEyeInfo(condition) {
        switch (condition) {
            case 'Normal':
                return {
                    name: 'NORMAL VISION',
                    details: 'Normal vision means your eyes are free from physically visible indications of a disease. It indicates that your eyes are functioning well without any noticeable issues.',
                    cause: 'Maintaining normal vision is often attributed to overall eye health and good habits.',
                    recommendations: [
                        'Eat a balanced diet rich in vitamins and minerals, particularly those beneficial for eye health like vitamin A, C, E, and omega-3 fatty acids.',
                        'Protect your eyes from harmful UV rays by wearing sunglasses outdoors.',
                        'Practice good eye hygiene, such as avoiding rubbing your eyes excessively and washing your hands regularly.',
                        'Take regular breaks when using digital screens for extended periods to reduce eye strain.',
                        'Ensure proper lighting when reading or working to prevent eye fatigue.',
                        'Get regular eye check-ups with an optometrist or ophthalmologist to monitor your eye health and detect any issues early.',
                    ],
                };
            case 'Cataract':
                return {
                    name: 'CATARACT',
                    details: 'Cataracts are cloudy areas that form on the lens of your eye. Your lens is a clear, flexible structure made mostly of proteins (crystallins). As you get older, the proteins in your lens break down, forming cloudy patches that affect your vision.',
                    cause: 'The main cause of cataracts is the gradual breakdown of proteins in your lens. However, certain genetic and environmental factors can raise your risk of developing cataracts or developing them at a younger age compared with others.',
                    symptoms: [
                        'Vision that’s cloudy, blurry, foggy, or filmy.',
                        'Changes in the way you see color (colors may look faded or not as vivid).',
                        'Sensitivity to bright sunlight, headlights, or lamps.',
                        'Glare, including halos or streaks that form around lights.',
                        'Difficulty seeing at night.',
                        'Changes in your vision prescription, including near-sightedness that gets worse.',
                        'Needing a brighter light to read.',
                        'Double vision.'
                    ],
                    treatments: 'Cataract surgery is the only way to remove cataracts and restore your clear vision. During cataract surgery, an ophthalmologist removes your clouded natural lens and replaces it with an intraocular lens (IOL). An IOL is an artificial lens that permanently stays in your eye. There are many different options for IOLs that your provider can discuss with you. </br></br> The main benefit of an IOL is that it’s clear — like your natural lens should be. Another benefit is that it can correct refractive errors, allowing you to rely less on glasses or contact lenses after your surgery.'
                };
            case 'Conjunctivitis':
                return {
                    name: 'CONJUNCTIVITIS',
                    details: 'Often referred to casually as “pink eye”, conjunctivitis is the swelling or inflammation of the conjunctiva, the thin, transparent layer of tissue that lines the inner surface of the eyelid and covers the white part of the eye.',
                    cause: 'The pink or reddish color of pink eye happens when the blood vessels in the membrane covering your eye (the conjunctiva) gets inflamed, making them more visible. Causes of inflammation include: Viruses, bacteria, allergens, irritating substances, sexually transmitted infections, a foreign object in your eye, blocked or incompletely opened tear ducts in babies, and autoimmune conditions.',
                    symptoms: [
                        'Redness in the white of your eye or inner eyelid.',
                        'Increased tearing.',
                        'Thick yellow discharge that crusts over your eyelashes, especially after sleep.',
                        'Green or white discharge from your eye.',
                        'Gritty feeling in one or both eyes.',
                        'Itchy eyes (especially in pink eye caused by allergies).',
                        'Burning eyes (especially in pink eye caused by chemicals and irritants).',
                        'Blurred vision.'
                    ],
                    treatments: 'The treatment for pink eye varies depending on the underlying cause, whether it’s bacterial, viral, allergenic, or due to an irritant. </br></br> Bacterial conjunctivitis typically requires antibiotics in the form of eye drops, ointments, or pills, while viral conjunctivitis often resolves on its own but may require antiviral medication for certain infections like herpes simplex or varicella-zoster. Irritant-induced conjunctivitis can be managed by rinsing the eyes with warm water to remove the irritant, with immediate medical attention needed for strong chemical exposures. Allergic conjunctivitis is treated with prescription or over-the-counter eye drops containing antihistamines or anti-inflammatory drugs, while pink eye caused by sexually transmitted infections or autoimmune diseases requires specific medical treatments tailored to the underlying condition. Additionally, newborns at risk of bacterial conjunctivitis are typically provided with antibiotic ointment as a preventive measure.',
                };
            case 'Ectropion':
                return {
                    name: 'ECTROPION',
                    details: 'Ectropion is the medical name for outward-facing eyelid. When you have ectropion, the inside of your eyelid can become irritated. The condition can happen to an upper or lower eyelid, but it often happens to the lower lid.',
                    cause: [
                        'Involutional ectropion is the most common type of ectropion. This can be associated with constant eye rubbing, but it’s most often related to aging eyelids. The eyelids get looser because muscles and ligaments get looser.',
                        'Paralytic ectropion happens along with facial nerve palsy, like Bell’s palsy. This type of palsy comes on quickly. It often causes drooping of one side of your face. A stroke can also cause cranial nerve paralysis.',
                        'Cicatricial ectropion can be caused by scars and by excessive and repeated sun exposure. You may have this type of ectropion if you’ve already had blepharoplasty (eyelid surgery) or any other type of eye injury, like burns or chemical irritation.',
                        'Mechanical ectropion happens when your lower eyelid is pulled away from the eye by some type of heavy weight. This could be a tumor, a mass of fat or edema (swelling, water retention.)',
                        'Congenital ectropion is the least common type. This is a type of outward-turning eyelid that you’re born with. Down syndrome and blepharophimosis syndrome are two congenital conditions that may make ectropion more likely.'
                    ],
                    symptoms: [
                        'Feeling like you have something in your eye.',
                        'Dryness.',
                        'Redness.',
                        'Tearing (watering) of the eye.'
                    ],
                    treatments: 'Your provider will almost always begin your treatment by prescribing artificial tears or other types of drops or ointments to add moisture to your eye. </br></br> If your provider thinks that eye drops you’ve been using over a long period of time are related to the ectropion, they will ask you to stop using these drops. Your condition may improve when the drops are stopped. </br></br> If the ectropion is related to a skin condition, your provider may first treat the skin condition and that may stop the ectropion. </br></br> After that, your healthcare provider is likely to suggest surgery to treat ectropion if you’re well enough to have surgery. Most of these kinds of surgeries are on an outpatient basis, meaning you can go home the same day. </br></br> If your healthcare provider is doing surgery on your lower eyelid for ectropion, they’ll remove part of the lid (usually at the outer edge of the eye) and reattach the ligaments in a tighter position. They’ll want to make sure that the lids fit together again and that the punctum (the hole where tears flow into the nasal cavity) is in the correct place. </br></br> Some ectropion surgeries may require a skin graft, such as surgery to correct scarring that causes ectropion. </br></br> In some cases, you may need more than one surgery to fix the ectropion completely.',
                };
            case 'Pterygium':
                return {
                    name: 'PTERYGIUM',
                    details: 'Pterygium (pronounced tur-IJ-ee-um) is a raised, fleshy growth on your eye’s conjunctiva. Your conjunctiva is the clear membrane that covers the white of your eye. Pterygium can affect one or both of your eyes but usually not at the same time. When it affects both eyes at the same time, it’s called bilateral pterygium.',
                    cause: [
                        'Long-term exposure to the sun’s ultraviolet (UV) light (most common cause).',
                        'Eye irritation from hot and dry weather, wind and dust.'
                    ],
                    symptoms: [
                        'A slightly raised pink growth on your eye.',
                        'Red, irritated or swollen eyes.',
                        'Dry eyes, itchy eyes or burning eyes.',
                        'Feeling like you have sand or grit is in your eye.',
                        'Teary eyes.',
                        'Increase in the size and spread of the lesion.',
                        'An unpleasant appearance of your eye due to the size of the lesion.',
                        'Blurred vision or double vision (if pterygium grows onto your cornea).'
                    ],
                    treatments: 'If your symptoms don’t cause discomfort or interfere with your vision, you probably don’t need treatment. Your provider will schedule office visits to see if the pterygium is growing or causing vision problems. </br></br> You may need surgery if eye drops and eye ointments aren’t relieving your symptoms, the pterygium grows so large that it blocks your vision or pulls on your cornea and changes its curve causing astigmatism, or if the way your eye looks is not acceptable to you.',
                };
            case 'Trachoma':
                return {
                    name: 'TRACHOMA',
                    details: 'Trachoma is an eye disease caused by a bacterium called Chlamydia trachomatis. The infection can cause irreversible blindness. It’s an issue in poor and rural areas throughout the world with poorer hygiene, limited access to clean water and sanitation, and problems with crowding.',
                    cause: 'Trachoma is a bacterial infection that starts out being a little bit like pink eye (conjunctivitis), with symptoms of redness, irritation and discharge. Trachoma spreads through personal contact, with infected discharge from eyes and noses touching other people’s hands or infected clothing or bedding. Flies can also spread the infectious discharge from one person to another. Symptoms can begin from five to 12 days after you’ve been exposed to the active infection.',
                    symptoms: [
                        'Red and irritated eyes.',
                        'Swollen eyelids.',
                        'Blurred vision.',
                        'Watery discharge from the eyes.',
                        'Discharge from the nose.',
                        'Tightened eyelids due to scar tissue.',
                        'Inward-turning eyelashes because of the tight eyelids.',
                        'Extreme eye pain caused by eyelashes scraping against your cornea.',
                        'Light intolerance.',
                        'Impaired vision, possible blindness.'
                    ],
                    treatments: 'In early stages, your provider can treat and cure trachoma by giving you antibiotics. The two drugs recommended for trachoma are azithromycin and an ointment made with tetracycline. </br></br>Trachoma that isn’t treated, or trachoma that happens repeatedly, can develop into trachomatous trichiasis. Your provider may suggest surgery. This can change the position of eyelashes so they no longer scrape your eye. This should prevent further scarring. </br></br>Severe damage to your cornea may lead your provider to recommend a corneal transplant. </br></br> If trachoma isn’t treated, you won’t be able to reverse the blindness that occurs.',
                };
            default:
                return {
                    name: 'Unknown',
                };
        }
    }
}


if (!DEBUG) {
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

    console.log("(script.js is running)");
    console.log(lightmodeurl);

    // Apply the theme from the stored preference
    if (document.body.classList.contains("light-theme")) {
        icon.src = lightmodeurl;
        console.log(lightmodeurl);
        if (assess) assess.src = lightassessurl;
        if (library) library.src = lightlibraryurl;
        if (nav_icon) nav_icon.src = navicon2url;
        console.log(navicon2url);
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
            icon.src = lightmodeurl;
            if (assess) assess.src = lightassessurl;
            if (library) library.src = lightlibraryurl;
            if (nav_icon) nav_icon.src = navicon2url;
            if (upload) upload.src = lightuploadurl;
            // Store the theme preference
            localStorage.setItem('theme', 'light-theme');
        } else {
            icon.src = darkmodeurl;
            if (assess) assess.src = darkassessurl;
            if (library) library.src = darklibraryurl;
            if (nav_icon) nav_icon.src = naviconurl;
            if (upload) upload.src = darkuploadurl;
            // Store the theme preference
            localStorage.setItem('theme', '');
        }
    }
}
console.log("Jan's code finished.")

/*START HERE*/
document.addEventListener('DOMContentLoaded', function () {
    var questions = document.querySelectorAll('.question');
    var answers = document.querySelectorAll('.answer');

    questions.forEach(function (question) {
        question.addEventListener('click', function () {
            var answer = this.nextElementSibling;
            var isActive = this.classList.contains('active');

            answers.forEach(function (otherAnswer) {
                if (otherAnswer !== answer && otherAnswer.style.display === 'block') {
                    otherAnswer.style.display = 'none';
                }
            });

            questions.forEach(function (q) {
                q.classList.remove('active');
            });

            if (!isActive || answer.style.display !== 'block') {
                this.classList.add('active');
            }

            answer.style.display = isActive ? 'none' : 'block';
        });
    });
});
/*END HERE*/

console.log("Question code has ended execution.");
















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

console.log("Original initializations finished.")

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
    console.log("Attempting submission...")
    upload_btn.click();
    console.log("Attempted submission.")

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



//RESULTS



//END HERE***************************************************************************