# from django.shortcuts import render

from django.shortcuts import redirect, render
from .models import Image
from .forms import ImageForm


# Import needed libraries for model integration and input processing
import tensorflow
import numpy as np
import efficientnet.tfkeras
from tensorflow.keras.preprocessing import image

import cv2
import glob

import os
import traceback

from pathlib import Path

## MODEL ##
# Load the saved model
loaded_model = tensorflow.keras.models.load_model('edr/model.h5')

# Print the class labels
class_labels = list(["Cataract", "Conjunctivitis", "Ectropion", "Normal", "Pterygium", "Trachoma"])

new_session = True

def index(request):
    
    # EWWWWW
    global new_session

    # print current directory for debuggings
    print("WORKING DIRECTORY: ")
    print(os.getcwd())

    # Remove previous session files
    if new_session:
        print("Clearing files from previous session...")
        root = Path('./media')
        filenames = ['sharingan'] # eto lang ang maliligtas

        for path in root.iterdir():
            if path.name not in filenames:
                path.unlink()
        new_session = False
    else:
        print("Clearing will proceed in the next session.")

    # PREPARE THE MODEL
    print("Preparing the model...")
    
    ## DATA PREPROCESS ##
    test_image_path = 'media/sharingan'
    img = image.load_img(test_image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.  # Normalize the image

    ## INPUT TO MODEL ##
    prediction = loaded_model.predict(img_array)

    ## RESULT ##
    # Get Result
    predicted_class = np.argmax(prediction, axis=-1)
    predicted_label = class_labels[predicted_class[0]] # The Output
    print("Sharingan!")
    print("Preloading Result: "+predicted_label)
    
    context = {}
    return render(request, "edr/index.html", context)

def disclaimer(request):
    context = {}
    return render(request, "edr/disclaimer_screen.html", context)

# def assess(request):
#     context = {}
#     return render(request, "edr/assess_screen.html", context)

def list(request):
    context = {}
    return render(request, "edr/list_screen.html", context)

def dis_library(request):
    context = {}
    return render(request, "edr/library.html", context)

def results(request, filename):
    '''
    # PSEUDOCODE
    do face_extraction on image
    if face_extracted:
        image = extracted face
    else if no face_extracted:
        write disclaimer for user
    
    do eye_extraction on image
    if eye_extracted:
        image = extracted eye
    else if no eye_extracted:
        write disclaimer for user
    '''

    # here we will store the face rectangle sizes
    rectangle_sizes = []
    # this will be the index of the biggest face rectangle
    biggest_rectangle = 0 
    
    extracted_face = False
    extracted_eye = False
    displayed_image = ""
    
    ## DATA PREPROCESS ##
    test_image_path = 'media/'+filename
    img_list = glob.glob(test_image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    for file in img_list:
        print(file)     # For checking
        img = cv2.imread(file, 1)  # Jovic: Now, we can read each file since we have the full path
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # FACE EXTRACTION
        faces, faceRejectLevels, faceLevelWeights = face_cascade.detectMultiScale3(gray, scaleFactor=1.3,
                                                     minNeighbors=5,
                                                     minSize=(10, 10),
                                                     flags=cv2.CASCADE_SCALE_IMAGE,
                                                     outputRejectLevels=True)
        try:
            # This tries to take the face with the highest confidence level
            # x, y, w, h = faces[np.argmax(faceLevelWeights)]
            if faces.size > 0:
                print("Faces:")
                print(faces)
                # Iterate over the faces and calculate the rectangle areas
                for i, face in enumerate(faces):
                    # Multiply the face length and width
                    rectangle_sizes.append(face[2]*face[3])
                    print(rectangle_sizes[i])
                # Now select the face with the max size
                x, y, w, h = faces[rectangle_sizes.index(max(rectangle_sizes))]
            # Proceed with the original procedure
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            resized = cv2.resize(roi_color, (500,500))
            cv2.imwrite("media/extracted.jpg", resized)
            test_image_path = "media/extracted.jpg"
            extracted_face = True
        except:
            print("FACE EXTRACTION WENT WRONG.")
            traceback.print_exc()
            extracted_face = False
            roi_gray = gray

        if extracted_face:
            # EYE EXTRACTION
            eyes, eyeRejectLevels, eyeLevelWeights = eye_cascade.detectMultiScale3(roi_gray, scaleFactor=1.3,
                                                            minNeighbors=5,
                                                            minSize=(10, 10),
                                                            flags=cv2.CASCADE_SCALE_IMAGE,
                                                            outputRejectLevels=True)
            print("EYES:")
            print(eyes)
            try:
                ex, ey, ew, eh = eyes[np.argmax(eyeLevelWeights)]
                if not extracted_face:
                    roi_color = img[ey:ey+eh, ex:ex+ew]
                roi_eye = roi_color[ey:ey+eh, ex:ex+ew]
                if not extracted_face:
                    resized = cv2.resize(roi_color, (128,128)) 
                else:
                    resized = cv2.resize(roi_eye, (128,128))
                cv2.imwrite("media/extracted.jpg", resized)
                test_image_path = "media/extracted.jpg"
                extracted_eye = True
            except:
                print("EYE EXTRACTION WENT WRONG.")
                traceback.print_exc()
                extracted_face = False



    img = image.load_img(test_image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.  # Normalize the image

    ## INPUT TO MODEL ##
    # Copied verbose=0 from Jan's confidence code
    prediction = loaded_model.predict(img_array, verbose=0)

    # Get confidence
    confidence = prediction[0, np.argmax(prediction)]
    confidence *= 100
    confidence_str = f"{confidence:.2f}%"

    ## RESULT ##
    # Get Result
    predicted_class = np.argmax(prediction, axis=-1)
    predicted_label = class_labels[predicted_class[0]].upper() # The Output
    # Output Result
    # return predicted_label
    if extracted_face or extracted_eye:
        displayed_image = "extracted.jpg"
    else:
        displayed_image = filename
    print(displayed_image)
    
    apology = ""
    reassess_prompt = ""
    if not extracted_face or not extracted_eye:
        apology = "Sorry, I can't extract your"
        if not extracted_face and not extracted_eye:
            # apology += " face and eye "
            apology += " face "
        # elif not extracted_face:
        #     apology += " face "
        # elif not extracted_eyes:
        #     apology += " eye "
        apology += " :(\n"
    reassess_prompt = "Please click Re-Assess if you think the assessment is inaccurate."

    # Just kidding, we still need to display the images
    # # AUTODELETION
    # # remove extracted.jpg
    # if os.path.isfile("./media/extracted.jpg"):
    #     os.remove("./media/extracted.jpg")
    # # remove original image
    # if os.path.isfile("./media/"+filename):
    #     os.remove("./media/"+filename)

    context = {'image': displayed_image, 'predicted_label': predicted_label, 'apology': apology, 'reassess_prompt': reassess_prompt, 'confidence': confidence_str}
    return render(request, "edr/results_screen.html", context)

def assess(request, valid_input=1):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    print("Loading Assess page...")
    # Handle file upload
    # This runs only on a POST request, triggered by a form submission
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print("Initialized form variable.")
        if form.is_valid():
            newimg = Image(imgfile=request.FILES['imgfile'])
            newimg.save()

            # TODO: If extension not in list of image file extensions
            # Get the extension of the file
            _, ext = os.path.splitext(newimg.imgfile.name)
            
            # Check if the extension is in the list of common image file extensions
            # if ext.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']:
            if ext.lower() not in ['.jpg', '.jpeg', '.png']:
                # Redirect back to assess again, this time with message for user
                return redirect('./0') # 0 parameter means message will be displayed, 1 means no



            # Redirect to the image list after POST
            print("Redirecting to results...")
            return redirect('results/'+newimg.imgfile.name) # this is where the filename argument comes from
        else:
            message = 'The form is not valid. Fix the following error:'
            print(message)
    # Othewise it is just a normal GET request
    else:
        form = ImageForm()  # An empty, unbound form
        print("Initialized empty, unbound form.")

    # Load images for the list page
    images = Image.objects.all()

    if valid_input == 0:
        message_str = "Please upload a JPG, JPEG, or PNG file!"
    else:
        message_str = ""

    # Render list page with the images and the form
    context = {'images': images, 'form': form, 'message_str': message_str}
    return render(request, 'edr/assess_screen.html', context)
    
def faq(request):
    context = {}
    return render(request, 'edr/faqs.html', context)
