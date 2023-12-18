#!/usr/bin/env python
# coding: utf-8

# Q1. Write statement to import NumPy?

# In[1]:


import numpy as np


# Q2. Create an array using NumPy?

# In[2]:


arr=np.array([1,2,3,4,5,6])
arr


# Q3. Create an array of 10 random integers?

# In[3]:


random_integers=np.random.randint(2,30,10)
random_integers


# Q4. Create an array of elements from 10-20?

# In[4]:


arr=np.arange(10,21)
arr


# Q5. Create an array which contains value 5,10 times?

# In[6]:


arr=np.repeat(5,10)
arr


# Q6. Create one dimensional array and convert that into 3*3 matrix?

# In[7]:


arr=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
arr


# Q7 Create a 2D array of size 3*3 but all the elements should be between 0 to 1?

# In[9]:


arr=np.random.rand(3,3)
arr


# Q8. Concatenate 2D array horizontally and vertically?

# In[11]:


arr1=np.array([1,2,3,4]).reshape(2,2)
arr2=np.array([5,6,7,8]).reshape(2,2)
horizontal_concatenate=np.hstack((arr1,arr2))
vertical_concatenate=np.vstack((arr1,arr2))
print(f"Horizontally concatenated array =\n {horizontal_concatenate}")
print(f"Vertically concatenated array =\n {vertical_concatenate}")

