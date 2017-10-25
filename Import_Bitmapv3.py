# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:43:52 2017

@author: fculfaz

This code gives the mean and standard deviation for a pre-selected Region of
Interest (ROI) within an image, for all images specified in the local path. It
then plots the mean and standard deviation with gain, where the gain values
are specified in the filename.

"""

import os
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from PIL import Image

#input your local path here
path = '//Sstnas002/opgprojects/554 - RemDB/Technical/MAIT/TestResults/20171020 - TDS Camera T Chamber Light Wall Gain Tests'

#create your arrays
Mean_Total = []
SD_Total = []
Min_Total = []
Max_Total = []
float()
Number_Total = []
bmp = []

#input ROI here in pixels
minr = 550
minc = 800 
maxr = 680
maxc = 930

#A for loop to process all the image files in your local folder
files = [f for f in os.listdir(path) if os.path.splitext(f)[-1] == '.bmp']

for file in files:
    im = np.array(Image.open(os.path.join(path, file))) 
    
    #Show the images
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(im)
    plt.title('Image: ' + file)
    
    #To draw the region of interest over the image file being processed  
    ROI= im[minr:maxr,minc:maxc] 
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                           fill=False, edgecolor='red', linewidth=2)
    ax.add_patch(rect)
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()
       
    #Print the image stats inside the region of interest      
    print('Mean =  {0:.3f}.'.format(ROI.mean()))
    Mean=ROI.mean()
    print('StD =  {0:.3f}.'.format(ROI.std()))
    SD=ROI.std()
    print('Min =  {0:.1f}.'.format(ROI.min()))
    Min=ROI.min()
    print('Max =  {0:.1f}.'.format(ROI.max()))
    Max=ROI.max()
    
    #Append these image stats from each image onto an array
    Mean_Total = np.append(Mean_Total, Mean)
    SD_Total = np.append(SD_Total, SD)
    Min_Total = np.append(Min_Total, Min)
    Max_Total = np.append(Max_Total, Max)
    number = float(file[13:16])
    Number_Total = np.append(Number_Total, number)

# Plot the mean and standard deviation within the ROI for each image    
plt.figure(2)
plt.scatter(Number_Total, Mean_Total, label = 'Data') # Mean vs. Gain
plt.title('Mean vs Gain')
plt.xlabel('Gain Setting')
plt.ylabel('Mean Signal in ROI (ADU)')

plt.figure(3)
plt.scatter(Number_Total, SD_Total, label = 'Data') # Standard Deviation vs. Gain
plt.title('StD vs Gain')
plt.xlabel('Gain Setting')
plt.ylabel('Standard Deviation of Signal in ROI (ADU)')