#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def redact_pii(text):
    text = re.sub(r'\b\d{6}[-+]\d{4}\b', '[REDACTED SSN]', text)
    text = re.sub(r'\+46[\s\d]{7,}', '[REDACTED PHONE]', text)
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[REDACTED EMAIL]', text)
    return text

