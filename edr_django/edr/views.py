# from django.shortcuts import render

from django.shortcuts import redirect, render
from .models import Image
from .forms import ImageForm


# Import needed libraries for model integration and input processing
import tensorflow
import numpy as np
import efficientnet.tfkeras
from tensorflow.keras.preprocessing import image

import os

## MODEL ##
# Load the saved model
loaded_model = tensorflow.keras.models.load_model('edr/model.h5')

# Print the class labels
class_labels = list(["Cataract", "Conjunctivitis", "Ectropion", "Normal", "Pterygium", "Trachoma"])

def index(request):
    #ATTEMPT AT PRELOADING
    print("Preloading model or something...")
    
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

def results(request, filename):
    ## DATA PREPROCESS ##
    test_image_path = 'media/'+filename
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
    # Output Result
    # return predicted_label
    context = {'image': filename, 'predicted_label': predicted_label}
    return render(request, "edr/results_screen.html", context)

def assess(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = Image(imgfile=request.FILES['imgfile'])
            newimg.save()

            # Redirect to the image list after POST
            return redirect('results/'+newimg.imgfile.name)
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = ImageForm()  # An empty, unbound form

    # Load images for the list page
    images = Image.objects.all()

    # Render list page with the images and the form
    context = {'images': images, 'form': form, 'message': message}
    return render(request, 'edr/assess_screen.html', context)