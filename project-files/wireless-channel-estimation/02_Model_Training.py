import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load the pre-processed data
X_train = np.load('X_train.npy')

# 2. Reshape for ConvLSTM (Adding the 'Time' dimension)
# We will treat our data as a sequence of 1 time step for this model
X_train = np.expand_dims(X_train, axis=1) # Shape becomes (8, 1, 128, 128, 2)

# 3. Define the ConvLSTM Architecture
model = models.Sequential([
    layers.Input(shape=(None, 128, 128, 2)), # Time, Height, Width, Channels
    layers.ConvLSTM2D(filters=32, kernel_size=(3, 3), padding='same', return_sequences=True),
    layers.BatchNormalization(),
    layers.ConvLSTM2D(filters=2, kernel_size=(3, 3), padding='same', return_sequences=True),
    layers.Activation('linear')
])

model.compile(optimizer='adam', loss='mse')
model.summary() # This will show the layers in your VS Code terminal

# 4. Train the Model (Using a small number of epochs for the test run)
print("Starting training...")
model.fit(X_train, X_train, epochs=20, batch_size=2)

# 5. Save the trained model
model.save('Final_Model.h5')
print("Model saved as Final_Model.h5")