import matplotlib.pyplot as plt

# Data from your 03_Evaluation_Baseline.py terminal output
results = [0.0004, 0.2607]# NMSE values for ConvLSTM and LS respectively 
labels = ['Proposed ConvLSTM', 'Traditional LS (Baseline)']
colors = ['#1f77b4', '#d62728'] # Professional blue and red

plt.figure(figsize=(9, 6))
bars = plt.bar(labels, results, color=colors, width=0.6)

# Adding the values on top of the bars for clarity
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.005, f'{yval:.4f}', ha='center', va='bottom', fontweight='bold')

plt.ylabel('Normalized Mean Square Error (NMSE)', fontsize=12)
plt.title('Final Performance Comparison: 128x128 Massive MIMO', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 0.4) # Setting a limit to show the gap clearly

# Save the image for your report
plt.savefig('Final_Performance_Comparison_1.png', dpi=300)
print("Graph saved as Final_Performance_Comparison_1.png")
plt.show()