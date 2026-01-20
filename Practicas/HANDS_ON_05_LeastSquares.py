# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

# Training set
x = [1, 2, 3]  
y = [1, 2, 2]
  
m = len(x)

# Model

  
# Cost function    

# dJ/dw    

# dJ/db    
    
# Gradient descent

 
plt.plot(wv,Jv)
plt.yscale('log')
plt.xlabel('w')
plt.ylabel('Jv')
plt.show()    

plt.plot(bv,Jv)
plt.yscale('log')
plt.xlabel('b')
plt.ylabel('J')
plt.show()   
#wva = np. array(wv)
#bva = np. array(bv)
#Jva = np. array(Jv)

plt.plot(wv)
plt.xlabel('iter')
plt.ylabel('w')
plt.show()    

plt.plot(bv)
plt.xlabel('iter')
plt.ylabel('b')
plt.show()   

plt.plot(Jv)
plt.yscale('log')
plt.xlabel('iter')
plt.ylabel('J')
plt.show()   

plt.plot(bv,wv)
plt.xlabel('b')
plt.ylabel('w')
plt.show()  