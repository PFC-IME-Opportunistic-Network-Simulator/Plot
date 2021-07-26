import matplotlib.pyplot as plt
import numpy as np
from services import getPointsFromFile

protocol = 'Direct Delivery' #nome deve ser o mesmo do arquivo
result = getPointsFromFile(protocol, 4)
velocityArray = result[0]
deliveryRatioArray = result[1]
deliveryDelayArray = result[2]

plt.plot(velocityArray, deliveryRatioArray, marker = 's')
plt.xticks(np.arange(0, 20, 2))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.title(protocol)
plt.xlabel('Node speed (m/s)')
plt.ylabel('Delivery ratio (%)')
plt.show()

plt.plot(velocityArray, deliveryDelayArray, marker = 's')
plt.xticks(np.arange(0, 20, 2))
plt.yticks(np.arange(0, 1200, 200))
plt.title(protocol)
plt.xlabel('Node speed (m/s)')
plt.ylabel('Average latency (s)')
plt.show()
