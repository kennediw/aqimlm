# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 10:07:52 2022

@author: Maurice Roots

AQI Machine Learning Model
Adapted from Kennedi White (aqimlm\final.ipynb)
"""

#%% Importing Packages

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import glob 

#%% 

beltsville_data_hourly = r'.\data\beltsville.csv'
hourly = pd.read_csv(beltsville_data_hourly)