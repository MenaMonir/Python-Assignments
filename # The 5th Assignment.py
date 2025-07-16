                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #             The 5st Assignment (Pandas)

# Task No.(1) Basic NumPy Operations
#             Objective:
#                       Practice creating NumPy arrays, performing basic operations, and using NumPy functions.

# ---/ (Import Numpy) /---
import numpy as np

# ---/ (Create Arrays) /---

a = [10,20,30,40,50]
array_a = np.array(a)               # 1 Dim-Array

b = [5,4,3,2,1]
array_b = np.array(b)  

# ---/ (Perform operations) /---

arr_sum = array_a + array_b  
print('Add the two arrays', arr_sum)

arr_sub = array_a - array_b
print('Subtract B from A ', arr_sub)

arr_mult = array_a * array_b
print('Multiblication ', arr_mult)

arr_Div = array_a / array_b
print(' Divide A by B ', arr_Div)

# ---/ (Apply NumPy Functions) /---

# ---/ Find the mean, maximum, and minimum of array A. /---

print(f"Min No.of array a is {array_a.min()}")
print(f"Max No.of array a is {array_a.max()}")
print(f"Sum for array a No is {array_a.sum()}")

# ---/ Calculate the dot product of A and B /---

dot_product_AB = np.dot(array_a,array_b)
print(f"Dot product of array(a) and array(B) is : {dot_product_AB}")

# ---/ Reshape array A into a 5x1 matrix /---

array_a__reshaped = array_a.reshape(5, 1)
print(f"Array A reshaped into a 5x1 matrix: \n{array_a__reshaped}")

# ---/ Check the shape of the new array /---
print(f"Shape of A_reshaped: {array_a__reshaped.shape}")