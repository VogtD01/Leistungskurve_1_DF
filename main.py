from load_data import load_data
import matplotlib.pyplot as plt
from sort import bubble_sort
import numpy as np

data=load_data('activity.csv')  

power_original = data['PowerOriginal']
# Sort the data
power_sorted = bubble_sort(power_original) 

#create plot
time = np.arange(0, len(power_original), 1)
plt.plot(time/60, power_sorted)
plt.xlabel("t / min")    
plt.ylabel("P / W")
plt.title("Power-Curve")
plt.show()

#save plot
plt.savefig("figures.png")

