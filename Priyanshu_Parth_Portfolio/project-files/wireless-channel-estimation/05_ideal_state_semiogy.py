import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

# 1. Your data
snr_range = [0, 5, 10, 15, 20]
nmse_ls = [0.35, 0.32, 0.30, 0.28, 0.2607] 
nmse_dnn = [0.02, 0.008, 0.002, 0.0009, 0.0004]

plt.figure(figsize=(9, 7))

# 2. Plotting
plt.semilogy(snr_range, nmse_ls, 'r--o', label='Traditional LS (Baseline)', linewidth=2)
plt.semilogy(snr_range, nmse_dnn, 'b-s', label='Proposed ConvLSTM', linewidth=2)

# 3. NATURAL FIX: Using LogFormatterSciNotation
# This tells Matplotlib to naturally use 1e-1, 1e-2 format only for powers of 10
ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.LogFormatterSciNotation(base=10))

# 4. Professional Formatting
plt.xlabel('SNR (dB)', fontsize=12, fontweight='bold')
plt.ylabel('Normalized Mean Square Error (NMSE)', fontsize=12, fontweight='bold')
plt.title('Final Model Performance: NMSE vs. SNR', fontsize=14, pad=15)
plt.grid(True, which="both", linestyle='--', alpha=0.3)
plt.legend(fontsize=11)

# Ensuring the limits allow at least 3-4 decades to appear naturally
plt.ylim(0.0001, 1.5) 

plt.savefig('Final_Semilogy_Results_2.png', dpi=300)
plt.show()