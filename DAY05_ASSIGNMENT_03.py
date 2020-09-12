#!/usr/bin/env python
# coding: utf-8

# # prime numbers using function

# In[264]:


def primenum(n):
    if (n<=1):
        return False
    elif(n!=2 and n%2==0):
        return False
    elif(n!=3 and n%3==0):
        return False
    elif(n!=5 and n%5==0):
        return False
    elif(n!=7 and n%7==0):
        return False
    else:
        return True


# In[265]:


lst=list(range(2500))


# In[266]:


print(list(filter(primenum,lst)))


# In[262]:





# In[ ]:





# In[ ]:




