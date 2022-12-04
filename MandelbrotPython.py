# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 22:15:00 2020

@author: joshu
"""


from numpy import linspace
from mpl_toolkits import mplot3d
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#1000 x and y values, lots of data. Can reduce to increase speed.
realx=linspace(-1.5,0.5,400)
imagy=linspace(-1,1,400)


z1=[]
z2bin=[]
for im_part in list(range(0,len(imagy))):
    z1.append([])
    z2bin.append([])
    print("Code is {}% complete".format(100*(im_part/len(imagy))))
    for real_part in list(range(0,len(realx))):
    
    
        z=0
        #c=1
        c=realx[real_part]+imagy[im_part]*1j
        for k in list(range(50)):
            z=z**2+c
        
        if abs(z)>50:
            z1set=1
        else:
            z1set=0
        
        z1[im_part].append(z1set)
        z2bin[im_part].append(z1set)
        



Y, X = np.meshgrid(imagy, realx)
matplotlib.pyplot.contourf(realx,imagy,z2bin)

"""
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(realx, imagy, z1, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D contour')
plt.show()
"""
            