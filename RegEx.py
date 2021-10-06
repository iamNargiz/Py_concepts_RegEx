#!/usr/bin/env python
# coding: utf-8

# In[11]:


#search() function
import re
text = "The match in Azerbaijan"
x = re.search('^The.*Azerbaijan$',text)
print(x)


# In[12]:


if x:
    print("Yes! We have a match!")
else:
    print("No match")


# In[13]:


#findall() function
txt = "The rain in Azerbaijan"
x = re.findall("ai", txt)
print(x)


# In[14]:


#No match
x = re.findall("Brazil", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[15]:


#split() function
x = re.split("\s", txt)
print(x)


# In[16]:


#split() with count
x = re.split("\s", txt, 1)
print(x)


# In[17]:


#sub() function
x = re.sub("\s", "%", txt)
print(x)


# In[10]:


#sub() with count
x = re.sub("\s", "%", txt, 2)
print(x)


# In[ ]:




