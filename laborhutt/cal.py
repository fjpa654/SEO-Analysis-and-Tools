# cal.py
import pandas as pd
from ei_ce import calculate_combined_weight

# Function to load data frames from CSV files
def load_data(filename):
    return pd.read_csv(filename)

# Load variables from CSV files into data frames
A_df = load_data('adjacency_matrix.csv')
C_df = load_data('click_through_rates.csv')
I_df = load_data('impressions.csv')

# Convert data frames to NumPy arrays
A = A_df.to_numpy()
C = C_df.to_numpy().reshape(-1)  # Reshape to convert 2D array to 1D
I = I_df.to_numpy().reshape(-1)  # Reshape to convert 2D array to 1D

# Constants
alpha = 0.5
beta = 0.3
gamma = 0.2

# Calculate combined weight vector
weights = calculate_combined_weight(A, C, I, alpha, beta, gamma)

# Print the result
print("Combined Weight Vector:", weights)
