#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install emoji')
import emoji

def convert_emoji_to_text(input_text):
    text_with_emoji = emoji.demojize(input_text)
    return text_with_emoji

# Example usage
input_text = "Hello! 🥳 How are you today? 🌈"
converted_text = convert_emoji_to_text(input_text)
print(converted_text)


# In[ ]:




