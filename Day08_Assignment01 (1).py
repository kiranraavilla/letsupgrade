#!/usr/bin/env python
# coding: utf-8

# In[34]:


def hai(hello):#getting one input using decorators
    def func_in():
        a=int(input("enter the input  :"))
        hello(a)
    return func_in
        
    
@hai
def fact(a):
    if(a<0):
        print("enter only positive number")
    elif(a==0 and a==1):
        print("factorial of {}".format(a))
    else:
        sum=1
        print("factorial 0f {}\n".format(a))
        for i in range(1,a+1):
            sum=sum*i
        print(sum)
        
@hai
def fibnocii(n):
    sum=0
    a=-1
    b=1
    if(n<0):
        print("enter only positive number")
    elif(n==0 or n==1):
         print(n)
    else:
         for i in range(0,n+1,1):
            sum=a+b
            a=b
            b=sum
            print(sum)
        


# In[18]:


fact()


# In[19]:


fact()


# In[20]:


fact()


# In[21]:


fact()


# In[22]:


fibnocii()


# In[36]:


fibnocii()


# In[35]:


fibnocii()


# In[38]:


fibnocii()


# In[41]:


def hello(chandru):

    def getInfo():
        a=int(input("enter the starting number : "))
        b=int(input("enter the ending number"))
        chandru(a,b)
    return getInfo


@hello
def oddEven(a,b):
    
    for i in range(a,b+1):
        if(i%2==0):
            print("{} is an even number ".format(i))

        else:
            print("{} is an odd number ".format(i))



@hello
def primeNumber(a,b):
    for i in range(a,b+1):
        if(i<=1):
            continue
        elif(i!=2 and i%2==0):
             continue
        elif(i!=3 and i%3==0):
             continue
        elif(i!=5 and i%5==0):
             continue
        elif(i!=7 and i%7==0):
              continue
        else:
            print("{} is a prime number".format(i))


# In[42]:


oddEven()


# In[43]:


primeNumber()


# In[ ]:




