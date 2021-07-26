import numpy as np
import matplotlib.pyplot as plt

def plotCDF(xArray, parameter, color, label):
    xCDFArray = []
    for x in xArray:
        x*=-parameter
        xCDFArray.append(x)
    
    yCDFArray = 1 - np.exp(xCDFArray)
    plt.plot(xArray, yCDFArray, "-"+color, label=label)

def getPointsFromFile(): 
    file = open("ExperimentalCDF.txt", "r")
    parameter = file.readline()
    line1 = file.readline()
    line2 = file.readline()
    file.close()

    parameter = float(parameter.rstrip('\n')) #remove '\n'

    line1 = line1.rstrip('\n')
    line1StringArray = line1.split(',')
    xPoints = np.array(line1StringArray).astype(np.float64)
    
    line2 = line2.rstrip('\n')
    line2StringArray = line2.split(',')
    yPoints = np.array(line2StringArray).astype(np.float64)
    return [xPoints, yPoints, parameter]
