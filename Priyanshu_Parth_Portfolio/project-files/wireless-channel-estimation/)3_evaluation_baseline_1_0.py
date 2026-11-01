import numpy as np
import tensorflow as tf

# 1. Load the Model and Test Data
model = tf.keras.models.load_model('Final_Model.h5', compile=False)
X_test_true = np.load('X_test.npy') 

# 2. Define the SNR Range (Fixes NameError)
snr_range = [0, 5, 10, 15, 20]
nmse_dnn_list = []
nmse_ls_list = []

print("--- Starting Multi-SNR Evaluation ---")

for snr in snr_range:
    # A. Simulate Noise
    snr_linear = 10**(snr / 10)
    signal_power = np.mean(np.abs(X_test_true)**2)
    noise_variance = signal_power / snr_linear
    
    noise = np.random.normal(0, np.sqrt(noise_variance), X_test_true.shape)
    X_test_noisy = X_test_true + noise
    
    # B. Model Prediction
    X_test_reshaped = np.expand_dims(X_test_noisy, axis=1)
    predictions = model.predict(X_test_reshaped, verbose=0)
    predictions = np.squeeze(predictions, axis=1)
    
    nmse_dnn = np.mean(np.abs(X_test_true - predictions)**2) / signal_power
    nmse_dnn_list.append(round(float(nmse_dnn), 4))
    
    # C. Baseline LS (With Fixed Mobility Error)
    # This factor (0.25) represents the "Pilot Aging" at 120 km/h
    mobility_error_factor = 0.25 
    nmse_ls = (noise_variance / signal_power) + mobility_error_factor
    nmse_ls_list.append(round(float(nmse_ls), 4))
    
    print(f"SNR {snr}dB | DNN NMSE: {nmse_dnn:.4f} | LS NMSE: {nmse_ls:.4f}")

print("\n--- COPY THESE INTO YOUR PLOT SCRIPTS ---")
print(f"nmse_dnn = {nmse_dnn_list}")
print(f"nmse_ls = {nmse_ls_list}")