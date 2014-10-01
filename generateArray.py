__author__ = 'glassman'
import random

def getArray(lenArray):
    randomarray = []
    i = 0
    while (i<random.randint(1,1000)):
        randomarray.append(random.uniform(0,10))
        i+=1
    return randomarray