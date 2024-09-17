#!/usr/bin/env python
# coding: utf-8

# SAEZ, ELJENZAL HOPER U.

# 2ECE - C

# NORMALIZATION PROBLEM

# In[21]:


import numpy as np

# creating a random 5x5 ndarray
X = np.random.rand(5, 5)

# calculate the mean and standard deviation
mean = X.mean()
std_dev = X.std()

# normalize the array using the given formula
X_normalized = (X - mean) / std_dev

# save the normalized array to a file
np.save('X_normalized.npy', X_normalized)

# print the results
print("Original Array:\n", X)
print("Normalized Array:\n", X_normalized)


# In[ ]:




