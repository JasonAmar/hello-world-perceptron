import numpy as np

class Perceptron(object):

    def __init__(self, n):

        self.n = n
        self.weights = np.random.uniform(-1,1,(self.n))
        self.c = 0.01
        
    def feedforward(self, inputs):

        my_sum = 0

        if (len(inputs)!= self.n):
            return "Incorrect input size"
        
        for i in range(self.n):
            my_sum += self.weights[i]*inputs[i]

        return (self.__activate(my_sum))

    def train(self, inputs, desired):
        
        guess = self.feedforward(inputs)
        error = float(desired - guess)

        for i in range (self.n):
            self.weights[i] += self.c*error*inputs[i]
            
    def __activate(self,my_sum):
        
        return (int(np.sign(my_sum)))
