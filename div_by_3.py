#!/usr/bin/env python
# coding: utf-8

# SAEZ, ELJENZAL HOPER U.

# 2ECE - C

# DIVISION BY 3 PROBLEM

# In[10]:


import numpy as np

# creating a 10x10 ndarray na may squares ng first 100 positive integers
X = np.arange(1, 101).reshape(10, 10) ** 2

# find kung anong elements yung divisible by 3
div_by_3 = X[X % 3 == 0]

# saving the result
np.save('div_by_3.npy', div_by_3)

# print the results
print("Original Array:\n", X)
print("Elements Divisible by 3:\n", div_by_3)


# In[ ]:




