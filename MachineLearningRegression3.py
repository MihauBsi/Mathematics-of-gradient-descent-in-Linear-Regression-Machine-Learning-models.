import math
from tkinter import Y
import numpy as np
import random
from sympy import Symbol, cos, diff, Derivative
import matplotlib as plt
import matplotlib.pyplot as plt

#http://www.learningaboutelectronics.com/Articles/How-to-find-the-partial-derivative-of-a-function-in-Python.php 
#https://mathinsight.org/partial_derivative_examples 
#https://www.khanacademy.org/math/ap-calculus-ab/ab-differentiation-2-new/ab-3-1a/v/chain-rule-introduction 
#https://pythonbasics.org/multiple-return/ 
#https://stackoverflow.com/questions/8429794/how-to-fill-a-list 

#Date Set
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,6,8,10,12,14,16,18,20] 
#th1 = random.sample(range(-1, 1), len(x))
#th2 = random.sample(range(-1, 1), len(x))

#Variables
th1 = []
th1.extend(range(-10, 10, 1))
th2 = []
th2.extend(range(-10, 10, 1))
Hyp = []
hJ = []
hJ2 = []

R1th = []
R2th = []
Mth = []

#The Hypothesis Function
def hypothesis(th1, th2, x):
    Hyp.append(th1 + th2*x)
    Hypothesis = (th1 + th2*x)
    return Hypothesis

#The Square Error Function
def J(th1,th2,x,y):
    for i in range(-100, 110):
        for n in range(-100, 110):
            R1th.append(i/10)
            R2th.append(n/10)
            Output = 0
            for m in range(len(x)):
                Output += ((hypothesis(i/10, n/10, x[m]) - y[m])**2)
            hJ.append((1/(2*len(x))) * Output)
            #print(Output)
    Mth.append(R1th)
    Mth.append(R2th)
    Mth.append(hJ)
    #print(Mth)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(R1th, R2th, hJ)
    ax.set_xlabel("Theta1)")
    ax.set_ylabel("Theta2")
    ax.set_zlabel("Loss")
    plt.show()
    return hJ



#print(J(th1,th2,x,y))
#print(Mth)

#The function for both Values of Theta
def SSq(temp0, temp1):
    a = 0
    a2 = 0
    for i in range(10):
        a += (hypothesis(temp0, temp1, x[i]) - y[i])
        a2 += ((hypothesis(temp0, temp1, x[i]) - y[i])*x[i])
    return a, a2

#Gradient Descent Function
def Gradient_Descent():
    J(th1,th2,x,y)
    alpha = 0.01
    temp0 = R1th[0]
    temp1 = R2th[0]
    Pre, Ro = 1, 2 
    while Pre != Ro: # Change this to an algorithm that checks if the last returned value is repeated, if so then print it.
        #temp0 = temp0 - alpha * ( (1/len(x) * hJ[i]) ) # Try to just use the Square Error function here with the Theta'a set to temp0 and temp1. Create new function that will sum over the Square Error function over all the values of x and the current values of the Theta's.
        t1, t2 = SSq(temp0, temp1)
        #temp1 = temp1 - alpha * ( (1/len(x) * hJ2[i]) )
        temp0 = temp0 - alpha * ((1/len(x) * t1))
        temp1 = temp1 - alpha * ((1/len(x) * t2))
        Theta1 = temp0
        Theta2 = temp1
        
        Pre, Ro = convergence(Theta1, Theta2) 
    return Theta1, Theta2

def convergence(Theta1, Theta2):    
    FOutput = 0
    Fy = 0     
    for n in range(0, len(x)):
        FOutput += Theta1 + Theta2*x[n]
        Fy += y[n]
    FOutput =  FOutput / len(x)
    Fy = Fy / len(x)
    return FOutput, Fy


print(Gradient_Descent())