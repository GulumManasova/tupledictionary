#!/usr/bin/env python
# coding: utf-8

# In[1]:


myfamily=("mother","father","sister","brother","sister")
print(myfamily)


# In[2]:


myfamily=("mother","father","sister","brother","sister")
print(type(myfamily))


# In[3]:


myfamily=("mother","father","sister","brother","sister")
print(myfamily[2])
print(myfamily[4])


# In[5]:


myfamily=("mother","father","sister","brother","sister")
y=list(myfamily)
y.append("me")
y=tuple(y)
print(y)


# In[7]:


myfamily=("mother","father","sister","brother","sister")
y=list(myfamily)
y.pop(3)
y=tuple(y)
print(y)


# In[ ]:




