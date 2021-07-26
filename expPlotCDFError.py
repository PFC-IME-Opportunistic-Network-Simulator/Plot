import matplotlib.pyplot as plt
import numpy as np
from services import plotCDF
from services import getPointsFromFile

result = getPointsFromFile()
xPoints = result[0]
yPoints = result[1]
parameter = result[2]

x = np.arange(0, 5, 0.1)
plotCDF(x, parameter, "r", 'original')
plt.plot(xPoints, yPoints, "-b", label="experimental")

plt.legend(loc="lower right")
plt.show()
