import numpy as np
import math as mth
activationType = {0: 'simple', 1:'sigmoida', 2: 'geneticAlg'}

class Neuron ():
    dataIn = None
    weightX = None
    out = None
    tableOfLearn = None
    countX = 0
    def __init__(self, data, weights):
        if (len(data) > 0):
            self.countX = len(data)

            if (self.countX == 0):
                self.dataIn = np.random.random(self.countX)
            else:
                self.dataIn = data

            if (len(weights) == self.countX):
                self.weightX = weights
            else:
                self.weightX = np.random.random(self.countX)
                weightSum = sum(self.weightX)
                for weight in self.weightX:
                    weight /= weightSum
        self.out = 0

    def print (self):
        if (self.countX > 0):
            for i in range (self.countX):
                print ("%d'st value = %f, weight = %f" % (i+1, self.dataIn[i], self.weightX[i]))
            print ("Out value = %f" % (self.out))
        else:
            print("no data in class")

    def summator (self):
        #обнуляем выход
        self.out = 0
        for i in range (self.countX):
            self.out +=self.dataIn[i]*self.weightX[i]

    def activate (self, typoAc, thresholdValue):
        if (typoAc == activationType[0]):
            if (self.out > thresholdValue):
                self.out = 1
            else:
                self.out = 0

    def initTableOfLearn (self):
        self.tableOfLearn = np.array([[0,0,0], [1,0,0], [0,1,0], [1,1,1]])

    def train (self):
        #error sum
        gError = 1.0
        #iteration count
        iterCount = 0.0
        self.initTableOfLearn()
        while gError != 0.0:
            gError = 0.0
            iterCount += 1
            dimLearn = self.tableOfLearn.shape
            for k in range (dimLearn[0]):
                #copy Learn data in Enters data
                self.dataIn = self.tableOfLearn[k:k+1, :(dimLearn[1]-1)]
                # Sum it
                self.summator()
                #Calculate error
                error = self.tableOfLearn[k][dimLearn[0]]
                #Sum of error in current data-module
                gError += np.abs(error)
                for m in range (self.countX):
                    #New weight = old weight + velocity + error + Enter-data
                    self.weightX[m] += 0.1 * error * self.dataIn[m]

    def __repr__(self):
        return repr(self.value)

#k = np.array([[1,2,3], [4,5,6], [7,8,9], [1,1,1]])
#print (k[1:2,0:2])

s = Neuron(np.array([1.66,100]), np.array([1,5]))
s.summator()
s.activate(activationType[0],0.1)
s.train()
s.print()