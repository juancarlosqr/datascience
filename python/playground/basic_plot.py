#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:13:21 2018

@author: jc
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
    
def draw_plot():
    x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    print(x)                     # Print datapoints
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.show()                   # Display the plot
    
if __name__ == '__main__':
    draw_plot()
