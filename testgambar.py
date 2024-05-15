from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

def proses_testing_gambar(image_path):
    # Load your pre-trained model
    model = load_model('ridho3.h5')

    # Dictionary to store the count of predicted classes
    class_count = {'Depression': 0, 'Healthy': 0}

    # Class labels mapping
    class_labels = {0: 'Depression', 1: 'Healthy'}

    # Function to process a single image
    def process_image(image_path):
        img = load_img(image_path, target_size=(16, 24))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions, axis=1)
        predicted_class = class_labels[predicted_class_index[0]]
        
        class_count[predicted_class] += 1

    # Process the single image file
    process_image(image_path)

    # Return the majority class detected and the counts
    majority_class = max(class_count, key=class_count.get)
    return majority_class, class_count

