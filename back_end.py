# Back End
# Imports
import tensorflow
import numpy as np
import efficientnet.tfkeras
from tensorflow.keras.preprocessing import image
# the above imports are the things you need to run this code.. which should be ok given that the tutorials are followed

## MODEL ##
# Load the saved model
loaded_model = tensorflow.keras.models.load_model('data\model\ignore\model.h5')

# Print the class labels
class_labels = list(["Cataract", "Conjunctivitis", "Ectropion", "Normal", "Pterygium", "Trachoma"])

def processInput(inputData):
    ## DATA PREPROCESS ##
    test_image_path = inputData
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
    return predicted_label