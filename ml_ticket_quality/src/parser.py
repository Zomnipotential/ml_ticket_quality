#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def parse_tickets(raw_text):
    chunks = re.split(r"(T-\d{4})", raw_text)
    raw_data = []
    for i in range(1, len(chunks), 2):
        ticket_id = chunks[i].strip()
        ticket_data = chunks[i + 1].strip()
        raw_data.append((ticket_id, ticket_data))

    final_table = []
    for ticket_id, chunk in raw_data:
        cleaned = re.sub(r'\s*\n+\s*', ' ', chunk.strip())

        created_at_match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+)\s*([\d:]+)', cleaned)
        if created_at_match:
            created_at = created_at_match.group(1) + created_at_match.group(2)
            after_created = cleaned[created_at_match.end():].strip()
        else:
            created_at = ""
            after_created = cleaned

        match = re.match(r'(\w+)\s+([\w\-]+)\s+\'(.+?)\'$', after_created)
        if match:
            channel = match.group(1)
            lang_hint = match.group(2)
            body = match.group(3).strip()
        else:
            channel = lang_hint = body = ""

        final_table.append({
            "ticket_id": ticket_id,
            "created_at": created_at,
            "channel": channel,
            "lang_hint": lang_hint,
            "body": body
        })

    return final_table

