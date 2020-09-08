import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y1 = [1, 2, 3, 4]
y2 = [2, 4, 6, 8]

plt.figure(num=3, figsize=(8, 8),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((0, 10))
plt.ylim((0, 10))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.show()