#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from src.parser import parse_tickets
from src.extractors import extract_entities
from src.scoring import score_ticket_components
from src.redact import redact_pii

import json
from pathlib import Path

import shutil
import os

# Load raw text input
with open("data/snippet.txt", "r", encoding="utf-8") as f:
    snippet = f.read()

# Parse and structure ticket data
tickets = parse_tickets(snippet)

# Extract entities, compute scores, redact bodies
for ticket in tickets:
    ticket["entities"] = extract_entities(ticket["body"])
    ticket.update(score_ticket_components(ticket))
    ticket["body_redacted"] = redact_pii(ticket["body"])

# Output: Save full and redacted reports
Path("output").mkdir(exist_ok=True)

with open("output/ticket_report_with_scores.json", "w", encoding="utf-8") as f:
    json.dump(tickets, f, indent=2, ensure_ascii=False)

# Create a clean redacted version with minimal fields and redacted body
redacted_version = []

for ticket in tickets:
    redacted_version.append({
        "ticket_id": ticket["ticket_id"],
        "created_at": ticket["created_at"],
        "channel": ticket["channel"],
        "lang_hint": ticket["lang_hint"],
        "body": ticket["body_redacted"],
    })

# Save redacted version
with open("output/ticket_report_redacted.json", "w", encoding="utf-8") as f:
    json.dump(redacted_version, f, indent=2, ensure_ascii=False)

# with open("output/ticket_report_redacted.json", "w", encoding="utf-8") as f:
#     json.dump(tickets, f, indent=2, ensure_ascii=False)

# Optional: print redacted output for control
print("\n=== Redacted Ticket Bodies ===\n")
for ticket in tickets:
    print(f"{ticket['ticket_id']}:\n{ticket['body_redacted']}\n{'-'*60}")



# Define paths
src = "output/ticket_report_with_scores.json"
dst = "../quality-api/src/main/resources/quality_report.json"  # adjust this if your Java project path is different

# Ensure the destination folder exists
os.makedirs(os.path.dirname(dst), exist_ok=True)

# Copy the file
try:
    shutil.copy(src, dst)
    print(f"Copied report to {dst}")
except Exception as e:
    print(f"Could not copy file: {e}")