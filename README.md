# ECE2112 - EXPERIMENT 2

## INTRODUCTION TO PYTHON PROGRAMMING

### Overview
This repository contains the code for Experiment 2 of the ECE2112 course, focusing on basic data preprocessing techniques using the NumPy library in Python. The experiments demonstrate how to normalize arrays and filter elements based on specific criteria.


#### I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Numpy library
2. To be able to apply and use the different codes and functions in creating a Python program using a Numpy library


#### II. Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. 


### A. Normalization of a Random Array

Normalization is one of the most basic preprocessing techniques in data analytics. This involves centering and scaling process. Centering means subtracting the data from the mean and scaling means dividing with its standard deviation. Mathematically, normalization can be expressed as

![Screenshot (1712)](https://github.com/user-attachments/assets/2fcc4be6-0924-4ac5-a148-a3ae4a719cf2)


In Python, element-wise mean and element-wise standard deviation can be obtained by using .mean() and .std() calls.

In this problem, create a random 5 x 5 ndarray and store it to variable X. Normalize X. Save your normalized ndarray as X_normalized.npy

#### Step-by-step Code Explanation

1. The script starts by creating a 5x5 array filled with random floating-point numbers between 0 and 1. This array is generated using NumPy’s np.random.rand function.
2. Next, the mean (average) and standard deviation of the values in the array are computed. The mean gives the central value of the array, while the standard deviation measures the spread of the values from the mean.
3. Then, use the formula Z = (Original Value - mean) / Standard Deviation. This transformation adjusts the range of values in the array to be centered around 0, with a consistent scale.
4. The normalized array is saved to a file (X_normalized.npy) using NumPy’s np.save function.
5. Print the results.


### B. Divisible by 3 Problem

Create the following 10 x 10 ndarray.

![Screenshot (1714)](https://github.com/user-attachments/assets/9fea055c-d9a9-4e99-85da-7338fb67f6ee)

which are the squares of the first 100 positive integers. From this ndarray, determine all the elements that are divisible by 3. Save the result as div_by_3.npy

#### Step-by-step Code Explanation

1. First, create a 10 by 10 array, where each element is the square of the integers from 1 to 100. This is done by creating a sequence of numbers from 1 to 100, squaring each number, and reshaping the resulting list into a 10x10 array.
2. Then, identify which of them are divisible by 3. We can do this by using NumPy’s array indexing to select elements where the modulo operation (% 3) equals 0.
3. Then, save the identified divisible by 3 elements to a file named div_by_3.npy. 
4. Print the results.

### Files

X_normalized.npy - Contains the normalized 5x5 ndarray.

div_by_3.npy - Contains the elements from the 10x10 ndarray that are divisible by 3.

### Contact

For any questions or feedback, please contact hopersaez@gmai.com
   
### Acknowledgements
Special thanks to the instructors and resources of the ECE2112 course for providing the foundational concepts.
