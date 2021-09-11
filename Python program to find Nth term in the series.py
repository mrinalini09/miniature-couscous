#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input())
t1=1
t2=2
cur=0
if(n>30):
    print("Invalid Input")
else:
    if(n==1 or n==2):
        print(n)
    else:
        for i in range(3,n+1):
            cur=t1+t2
            t1=t2
            t2=cur
            print(cur)
            


# In[ ]:




