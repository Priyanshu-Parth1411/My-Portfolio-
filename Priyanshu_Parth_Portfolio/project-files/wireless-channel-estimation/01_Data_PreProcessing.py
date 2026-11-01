import numpy as np
from sklearn.model_selection import train_test_split

# 1. Load the data you generated from data_gen.py
raw_data = np.load('mimo_data_raw.npy')

# 2. Normalization (Scaling)
# Neural networks perform best when data is between -1 and 1 or 0 and 1
# We normalize based on the maximum value in the dataset
max_val = np.max(np.abs(raw_data))
normalized_data = raw_data / max_val

# 3. Create 'Labels' for the model
# In Channel Estimation, the model tries to predict the 'True' channel (y) 
# from the 'Noisy' version (x). 
# For now, we split the data into training and testing sets.
X_train, X_test = train_test_split(normalized_data, test_size=0.2, random_state=42)

# 4. Save the processed files for the training script
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)

print(f"Pre-processing complete.")
print(f"Training set shape: {X_train.shape}") # Should show (Samples, Time, 128, 128, 2)