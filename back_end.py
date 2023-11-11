# Back End
# Imports
import tensorflow
import numpy as np
from tensorflow.keras.preprocessing import image
# the above imports are the things you need to run this code.. which should be ok given that the tutorials are followed

## MODEL ##
# Load the saved model
loaded_model = tensorflow.keras.models.load_model('data\model\ignore\model_conjunct_cataract_trachoma_normal.h5')

# Print the class labels
class_labels = list(["Cataract", "Conjunctivitis", "Normal", "Trachoma"])

## DATA PREPROCESS
inputimage = "cataract_input"
test_image_path = "data\input\\" + inputimage + ".jpg"
img = image.load_img(test_image_path, target_size=(256, 256))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.  # Normalize the image
# Input to Model
prediction = loaded_model.predict(img_array)

## RESULT ##
# Get Result
predicted_class = np.argmax(prediction, axis=-1)
predicted_label = class_labels[predicted_class[0]]
# Output Result
print("The predicted class is:", predicted_label)