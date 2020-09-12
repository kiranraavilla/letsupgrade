#!/usr/bin/env python
# coding: utf-8

# # error handling 

# In[8]:


try:
    file=open("chandru.txt","r")
    file.write("how are you?!!")
    file.close
except :
       print("Donot try , you cannot write!!!")
finally : print("Sucessfully completed")


# In[ ]:




