from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

def proses_testing(combined_image):
    # Load your pre-trained model
    model = load_model('ridho3.h5')

    # Directory containing images for prediction
    testing_dir = combined_image

    # Dictionary to store the count of predicted classes
    class_count = {'Depression': 0, 'Healthy': 0}

    # Function to process the directory
    def process_directory(directory):
        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(directory, file)
                img = load_img(img_path, target_size=(16, 24))
                img_array = img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                
                predictions = model.predict(img_array)
                predicted_class_index = np.argmax(predictions, axis=1)
                predicted_class = class_labels[predicted_class_index[0]]
                
                class_count[predicted_class] += 1

    # Class labels mapping
    class_labels = {0: 'Depression', 1: 'Healthy'}

    # Proses filenya
    process_directory(testing_dir)

    # return mayoritas kelas yang dideteksi
    majority_class = max(class_count, key=class_count.get)
    return majority_class, class_count