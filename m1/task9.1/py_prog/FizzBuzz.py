#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Fizz Buzz program
 
for fizzbuzz in range(1, 100): 
 
    # If number divided by 3 and 5 without rest, print “FizzBuzz”
    if fizzbuzz % 15 == 0: 
        print("FizzBuzz")                                         
        continue
 
    # If number divided by 3 without rest, print “Fizz”
    elif fizzbuzz % 3 == 0:     
        print("Fizz")                                         
        continue
 
    # If number divided by 5 without rest, print “Buzz”
    elif fizzbuzz % 5 == 0:         
        print("Buzz")                                     
        continue
 
    # Print numbers
    print(fizzbuzz)


# In[ ]:




