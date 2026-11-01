import numpy as np

def generate_time_varying_channel(Nt, Nr, velocity_kmh, fc=28e9, fs=1e6, num_steps=500):
    """
    Generates a time-varying Massive MIMO channel matrix.
    Nt: Transmit Antennas (e.g., 128)
    Nr: Receive Antennas (e.g., 128)
    velocity_kmh: Speed in km/h (e.g., 120 for high mobility)
    """
    c = 3e8  # Speed of light
    v = velocity_kmh / 3.6  # Convert to m/s
    fd = (v * fc) / c  # Max Doppler shift
    
    # Time vector for the duration of one frame
    t = np.arange(num_steps) / fs
    
    # Initialize 4D Channel: [Time, Nr, Nt, Real/Imag]
    H_series = []
    
    for step in t:
        # For high-mobility, the channel at each step is correlated
        # Jakes' approximation: h(t) = h(0) * Bessel(2*pi*fd*t)
        # Simplified for simulation:
        phase_shift = np.exp(1j * 2 * np.pi * fd * step)
        
        # Base Rayleigh channel (sparse in angular domain)
        H_base = (np.random.randn(Nr, Nt) + 1j*np.random.randn(Nr, Nt)) / np.sqrt(2)
        H_step = H_base * phase_shift
        
        # Split into Real and Imag for Deep Learning input
        H_combined = np.stack([H_step.real, H_step.imag], axis=-1)
        H_series.append(H_combined)
        
    return np.array(H_series)

# Base Test
Nt, Nr = 128, 128
data = generate_time_varying_channel(Nt, Nr, velocity_kmh=120)
print(f"Generated sequence shape: {data.shape}") 
# Expected: (10 steps, 128, 128, 2)
# Save the generated data to a file
np.save('mimo_data_raw.npy', data) 
print("Data saved successfully as mimo_data_raw.npy")