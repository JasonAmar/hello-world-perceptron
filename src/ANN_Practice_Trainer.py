import numpy as np

class Trainer(object):
    
    def __init__(self):
        self.bias = 1.0

    def __f(self,x):
        return (2*x + 1)

    def Inputs(self,array):
        return (np.append(array,[self.bias]))
    
    def Output(self,array):
        yline = self.__f(array[0])
        return(int(np.sign(array[1] - yline)))

