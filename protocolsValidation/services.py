import numpy as np
import matplotlib.pyplot as plt

def getPointsFromFile(fileName, numberOfPoints): 
    file = open(fileName, "r")
    velocityArray = []
    deliveryRatioArray = []
    deliveryDelayArray = []
    for i in range(numberOfPoints):
        velocity = float(file.readline())
        velocityArray.append(velocity)

        deliveryRatio = float(file.readline())
        deliveryRatioArray.append(deliveryRatio)

        deliveryDelay = float(file.readline())
        deliveryDelayArray.append(deliveryDelay)
        
    return [velocityArray, deliveryRatioArray, deliveryDelayArray]
