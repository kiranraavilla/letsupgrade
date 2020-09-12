#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class bank:
     def __init__(self,owner_name,balance):
        self.owner_name=owner_name
        self.balance= balance
     def deposit(self):
             amount=int(input("enter the amount to be deposited "))
             print("customer name ",self.owner_name)
             
             amount+=self.balance
             self.balance=amount
             print("your balance is ",amount)


     def withdraw(self):
            with_draw=int(input("enter amount to be withdrawn "))
            print("owner_name",self.owner_name)
            
            if(self.balance<with_draw):
                print("insufficient balance")
                print("your balance",self.balance)
                print("---transaction incomplete------")
            else:
                amount=self.balance-with_draw
                self.balance=amount
                print("your balance",amount)
                print("-----------transaction completed------------")
     


# In[ ]:


account=bank("chandru",40000)


# In[ ]:


account.withdraw()


# In[ ]:


account.deposit()


# In[ ]:





# In[ ]:




