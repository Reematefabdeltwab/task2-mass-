#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import *
seq = AASequence.fromString("DFPI")


# In[2]:


mfull = seq.getMonoWeight()
print("Monoisotopic mass of peptide [M] is", mfull)


# In[3]:


for i in seq:
   print(i.getMonoWeight())


# In[9]:


sum=0
for i in seq:

    sum += i.getMonoWeight()
    
print(sum)


# In[10]:


print ("mass of 'DFPI' less than mass of 'D'+'F'+'P'+'I'")


# In[ ]:




