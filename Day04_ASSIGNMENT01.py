#!/usr/bin/env python
# coding: utf-8

# In[5]:


lower = 1042000
upper = 702648265

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
       break


# In[ ]:





# In[ ]:




