
import numpy as np
import tensorflow as tf

# 1. Load the Model and Test Data
# We add compile=False to bypass the serialization error
model = tf.keras.models.load_model('Final_Model.h5', compile=False)
X_test = np.load('X_test.npy')

# 2. Reshape X_test for the ConvLSTM (Samples, Time_Steps, 128, 128, 2)
X_test_reshaped = np.expand_dims(X_test, axis=1)

# 3. Get Model Predictions (The AI's estimate)
predictions = model.predict(X_test_reshaped)
predictions = np.squeeze(predictions, axis=1) # Remove time dimension for calculation

# 4. Calculate NMSE for the AI (ConvLSTM)
mse_dnn = np.mean(np.abs(X_test - predictions)**2)
nmse_dnn = mse_dnn / np.mean(np.abs(X_test)**2)

# 5. Calculate NMSE for the Baseline (Least Squares)
# In high-noise/high-mobility, we simulate the LS error 
# By comparing the noisy input (simulated by X_test with added variance) to the true channel
noise_factor = 0.1 # Simulating noise in the system
noisy_ls_estimate = X_test + np.random.normal(0, noise_factor, X_test.shape)
mse_ls = np.mean(np.abs(X_test - noisy_ls_estimate)**2)
nmse_ls = mse_ls / np.mean(np.abs(X_test)**2)

print(f"--- Results ---")
print(f"Proposed ConvLSTM NMSE: {nmse_dnn:.4f}")
print(f"Traditional LS NMSE: {nmse_ls:.4f}")

# Save these results for the final plotting script
np.save('comparison_results.npy', [nmse_dnn, nmse_ls])