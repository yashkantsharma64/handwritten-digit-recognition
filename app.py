from flask import Flask, jsonify, render_template
import numpy as np
import pyscreenshot
import tensorflow as tf
import os
import cv2


def preprocess_image(img):
    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Resize to 28x28 pixels
    img_resized = cv2.resize(img_gray, (28, 28), interpolation=cv2.INTER_AREA)
    # Invert colors (if necessary)
    img_inverted = cv2.bitwise_not(img_resized)
    # Normalize pixel values
    img_normalized = img_inverted / 255.0
    # Reshape to match model input shape (add batch dimension)
    img_reshaped = np.expand_dims(img_normalized, axis=0)
    return img_reshaped

def predict():
    model = tf.keras.models.load_model('digit_recognition')
    img_num = 1
    while os.path.isfile(f"digits/digit{img_num}.png"):
        try:
            img = cv2.imread(f"digits/digit{img_num}.png")
            processed_img = preprocess_image(img)
            prediction = model.predict(processed_img)
            predicted_digit = np.argmax(prediction)
        except Exception as e:
            return jsonify({'error': str(e)})
        img_num += 1
    return predicted_digit

def image_capture():
    im = pyscreenshot.grab(bbox=(585, 375, 1330, 870))
    im.save("digits/digit1.png")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def handle_predict():
    image_capture()
    predicted_digit = predict()
    return jsonify({"result": int(predicted_digit)})

if __name__ == "__main__":
    app.run(debug=True)
