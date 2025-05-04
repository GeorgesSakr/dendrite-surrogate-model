# correct_train_test_split_usb.py

import numpy as np
import os
import json
from sklearn.model_selection import train_test_split

# Set the correct dataset path
dataset_dir = r"D:\dataset100100"  # notice the r to allow backslashes
train_fraction = 0.8

# Load metadata
metadata_path = os.path.join(dataset_dir, "metadata.json")
with open(metadata_path, "r") as f:
    metadata = json.load(f)

# Prepare input and output lists
inputs = []
outputs = []

for entry in metadata:
    run_id = entry["run_id"]
    xi_filename = entry["filename_xi"]
    
    # Load xi_series
    xi_series = np.load(os.path.join(dataset_dir, xi_filename))
    
    # Take only the final frame
    xi_final = xi_series[-1]  # shape (ny, nx)
    
    # Form input vector
    param_vector = [
        entry["dT0"],
        entry["c"],
        entry["N"],
        entry["theta_deg"],
        entry["seed_radius"]
    ]
    
    inputs.append(param_vector)
    outputs.append(xi_final)

# Convert lists to numpy arrays
X = np.array(inputs)  # shape (n_samples, 5)
Y = np.array(outputs) # shape (n_samples, ny, nx)

# Perform train/test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size=train_fraction, random_state=42
)

print(f"✅ Dataset split complete:")
print(f"  - Train inputs shape: {X_train.shape}")
print(f"  - Train outputs shape: {Y_train.shape}")
print(f"  - Test inputs shape:  {X_test.shape}")
print(f"  - Test outputs shape: {Y_test.shape}")

# Save the splits
np.save(os.path.join(dataset_dir, "X_train.npy"), X_train)
np.save(os.path.join(dataset_dir, "Y_train.npy"), Y_train)
np.save(os.path.join(dataset_dir, "X_test.npy"), X_test)
np.save(os.path.join(dataset_dir, "Y_test.npy"), Y_test)

print(f"✅ Files saved in {dataset_dir}")
