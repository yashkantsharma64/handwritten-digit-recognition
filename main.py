import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Load the MNIST dataset and preprocess it
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = X_train / 255  # Normalize pixel values to range [0, 1]
X_test = X_test / 255

# Define the neural network architecture
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Flatten 28x28 images into a vector
model.add(Dense(128, activation='relu'))  # Dense layer with 128 neurons and ReLU activation
model.add(Dense(128, activation='relu'))  # Another dense layer with 128 neurons and ReLU activation
model.add(Dense(10, activation='softmax'))  # Output layer with 10 neurons for 10 classes (digits 0-9) and softmax activation

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=25, validation_split=0.2)

# Save the trained model
model.save('digit_recognition')

# Load the saved model
model = tf.keras.models.load_model('digit_recognition')

# Predict on a test sample and print the predicted digit
print("Digit:", model.predict(X_test[1].reshape(1, 28, 28)).argmax(axis=1))

# Visualize the test sample
plt.imshow(X_test[1])
plt.show()
