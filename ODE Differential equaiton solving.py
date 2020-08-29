#!/usr/bin/env python
# coding: utf-8

# ## My Differential eqn solving

# $\frac{dy}{dt} = -k*y$

# k=0.2
# 

# y0=12

# In[2]:


#Import what we need
import numpy as np      
from scipy.integrate import odeint   # for differential eqn solving
import matplotlib.pyplot as plt


# In[9]:


#define class 'ordinary'

def ordinary(y,t):
    dydt = -k*y
    return dydt


# In[10]:


k = 0.2
y0=18 #we need to define y0 as default  for t when y = 0
t=np.linspace(0,20,100) #to plot the graph from where we get different values of t


# In[11]:


y = odeint(ordinary,y0,t)
plt.plot(y,t,'r',linewidth=2)
plt.xlabel('time')
plt.title('differential eqn graph')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()


# In[12]:



#What happen if we want to include scatter plot also

y=odeint(ordinary,y0,t)
plt.plot(y,t,'r',linewidth=2)
plt.xlabel('time')
plt.title('differential eqn graph')
plt.ylabel('y(t)')
plt.grid(True)
plt.scatter(y,t)
plt.show()


# # Making plots for different k values in a single graph
# k=0.1,k=0.2,k=0.3
# 

# In[21]:


def ordinary(y,t,k): #see here we include 'k' also
    dydt=-k*y
    return dydt
y0=12 
t=np.linspace(0,20,50)
k=0.1
y1=odeint(ordinary,y0,t,args=(k,))   #args=arguments , see what happened when we remove "args=(k,)"
k=0.2
y2=odeint(ordinary,y0,t,args=(k,))
k=0.3
y3=odeint(ordinary,y0,t,args=(k,))
plt.plot(t,y1,'r',linewidth=2,label='k=0.1')
plt.plot(t,y2,'b',linewidth=2,label='k=0.2')
plt.plot(t,y3,'g',linewidth=2,label='k=0.3')
plt.title('comparative graphs')
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()

plt.show()
#print(y)


# In[23]:


#print(model(y,0.2,k))


# # Reference: https://github.com/Daya-Ram/Differential-eqn-solving 

# In[ ]:




