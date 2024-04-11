from load_data import load_data
import matplotlib.pyplot as plt
from sort import bubble_sort
import numpy as np

data=load_data('activity.csv')  

power_original = data['PowerOriginal']
power_sorted = bubble_sort(power_original)  # Sort the data

plt.show()
time = np.arange(0, len(power_original), 1)
plt.plot(time/60, power_sorted)
plt.xlabel('Time (minutes)')    
plt.ylabel('Power (W)')


plt.show()
print(np.size(power_original))

