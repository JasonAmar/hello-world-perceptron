import ANN_Practice_Perceptron as P
import ANN_Practice_Trainer as T
import numpy as np

p = P.Perceptron(3)
t = T.Trainer()
i=0
desired = 0

try:
    f = open("PerceptronWeights.txt","r")
    if f.mode == "r":
        weights = f.read()
        weights = weights.split(",")
        weights = [float(i) for i in weights]
        p.weights = weights

except:
    for i in range(200000):
        inputs = np.random.uniform(-100,100,2)
        desired = t.Output(inputs)
        inputs = t.Inputs(inputs)
        p.train(inputs,desired)

    weights = ''.join([str(p.weights[i]) + "," for i in range(len(p.weights) - 1)]) + str(p.weights[len(p.weights)-1])
    f = open("PerceptronWeights.txt","w+")
    f.write(weights)
    f.close()

x = 0
y = 0
result = 0
while (True):
    print (" ")
    x = input("Input an x-coordinate: ")
    y = input("Input a y-coordinate: ")

    print (" ")
    result = p.feedforward([float(x),float(y),1.0])
    
    if result < 0:
        print ("Your XY point lies BELOW the line y = 2x + 1")

    else:
        print ("Your XY point lies ABOVE the line y = 2x + 1")
