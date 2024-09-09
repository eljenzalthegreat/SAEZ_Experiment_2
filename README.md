A. Normalization of a Random Array
   
This script generates a random 5x5 array of floating-point numbers between 0 and 1. It then normalizes the array by subtracting the mean and dividing by the standard deviation. The normalized array is saved to a file and both the original and normalized arrays are printed.

1. The script starts by creating a 5x5 array filled with random floating-point numbers between 0 and 1. This array is generated using NumPy’s np.random.rand function.
2. Next, the mean (average) and standard deviation of the values in the array are computed. The mean gives the central value of the array, while the standard deviation measures the spread of the values from the mean.
3. Then, use the formula Z = (Original Value - mean) / Standard Deviation. This transformation adjusts the range of values in the array to be centered around 0, with a consistent scale.
4. The normalized array is saved to a file (X_normalized.npy) using NumPy’s np.save function.
5. Print the results.

B. Divisible by 3 Problem

This script creates a 10x10 NumPy array where each element is the square of integers ranging from 1 to 100. It then identifies and extracts elements from this array that are divisible by 3. 

1. I first created a 10 by 10 array, where each element is the square of the integers from 1 to 100. This is done by creating a sequence of numbers from 1 to 100, squaring each number, and reshaping the resulting list into a 10x10 array.
2. I then identified which of them are divisible by 3. I did this by using NumPy’s array indexing to select elements where the modulo operation (% 3) equals 0.
3. Then, I saved the identified divisible by 3 elements to a file named div_by_3.npy. 
4. Print the results.
   
