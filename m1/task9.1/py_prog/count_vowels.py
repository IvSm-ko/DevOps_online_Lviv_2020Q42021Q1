#!/usr/bin/env python
# coding: utf-8

# In[4]:


# counting vowels in input text
vowels = ['а', 'е', 'и', 'і', 'ї', 'я', 'у', 'ю', 'є', 'о', 'А', 'Е', 'И', 'І', 'Ї', 'Я', 'У', 'Ю', 'Є', 'О']
Sentence = input("Введіть фразу: ")
count = 0
for letter in Sentence:
    if letter in vowels:
        count += 1
print(count)


# In[ ]:




