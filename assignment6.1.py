
# coding: utf-8

# In[3]:


import numpy as np

a1 = np.array([1,2,3,4])
print(a1)

N= 6

np.vander(a1,N,increasing=True)

