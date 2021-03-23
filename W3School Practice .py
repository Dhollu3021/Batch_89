#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("jyoti is my wife ")


# In[7]:


if (5 > 2):
 print ("5 is greater then 2")


# In[8]:


x=5 
y="jyoti"


# In[11]:


print(x)


# In[12]:


print(y)


# In[20]:


x="Jyoti fights with the Vaibhav"


# In[21]:


print(x)


# In[22]:


x=4  # this is int type 


# In[23]:


y="jyoti"   # this is string type values 


# In[24]:


print(x)


# In[25]:


print(y)


# In[26]:


#casting in the variable types 
x= str(3)  # x will be '3'
y= int(3)  # y will be 3
z= float(3)  # z will be 3.0


# In[27]:


print(x)


# In[28]:


print(y)


# In[29]:


print(z)


# In[30]:


#legal variable name in the python 


# In[32]:


_Jyoti_Dust='Vaibhav'


# In[33]:


print(_Jyoti_Dust)


# In[34]:


# assign multiples values at one place 
x,y,z="Orange", "Banana", "Cherry"


# In[35]:


print(x) #assign multiples values at one place 


# In[36]:


print(y)


# In[37]:


print(z)


# In[38]:


# for variabe we can use + sign to add two variable and print in one sentence 


# In[39]:


x='vaibhav'


# In[40]:


y='chotta jhutta'


# In[41]:


z=x+y


# In[43]:


print(z)


# In[45]:


# you can only concatenate the string not integer values 


# In[46]:


#gloabl variables 


# In[47]:


#the variables which are created outside of the functions is called gloabl variables 


# In[50]:


x='jyoti'
def vaibhav():
 print(x)
vaibhav()


# In[55]:


#If you use the global keyword, the variable belongs to the global scope:
x = 'bhadwa'
def myfunc():
  global x
  x = "fantastic"
print(x)
myfunc()

print("Python is " + x)


# In[56]:


# Python Data Types needs to understnd properlly very well otherwise it will create the issues while in the future 


# In[57]:


#type() is used to identify the value of data types 


# In[58]:


print(type(x))


# In[59]:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# In[ ]:




