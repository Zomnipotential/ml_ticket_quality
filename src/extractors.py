#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def extract_entities(body):
    entities = {}

    match = re.search(r'kundnr\s+(\d+)', body, re.IGNORECASE)
    entities['customer_id'] = match.group(1) if match else None

    match = re.search(r'felkod\s+(\d+)', body, re.IGNORECASE)
    entities['error_code'] = match.group(1) if match else None

    match = re.search(r'(\w+)-kontoret', body, re.IGNORECASE)
    entities['office_city'] = match.group(1) if match else None

    match = re.search(r'\b(exporterar fakturor|synkar|skickar|hämtar|laddar|loggar|sparar)\b', body, re.IGNORECASE)
    entities['action'] = match.group(1).lower() if match else None

    match = re.search(r'\b(\d{6}[-+]\d{4})\b', body)
    entities['personnummer'] = match.group(1) if match else None

    match = re.search(r'\+46[\s\d]{7,}', body)
    entities['phone'] = match.group(0).strip() if match else None

    match = re.search(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', body)
    entities['email'] = match.group(0) if match else None

    return entities

