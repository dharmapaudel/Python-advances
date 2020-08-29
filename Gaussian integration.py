#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Gaussian Integration 


# In[16]:


from numpy import ones,copy,cos,tan,pi,linspace
#defining the new function gaussxw 
def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w



# # Solve the following integral using Gaussian integral method
# $$ \int_0^2(x^4-2x+1)dx $$

# In[ ]:



def f(x):
    return x**4 - 2*x +1
N = 3
a = 0.0
b = 2.0


# In[18]:


x,w = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w


# In[19]:


s = 0.0
for k in range (N):
    s += wp[k]*f(xp[k])
print(s)


# In[ ]:


References
[1].Newman,M.(2013). Computational physics.CreateSpace Independent Publication. 

