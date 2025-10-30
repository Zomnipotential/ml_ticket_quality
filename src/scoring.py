#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def validate_personnummer(pnr: str) -> bool:
    if not pnr or not re.match(r"\d{6}[-+]\d{4}", pnr):
        return False
    digits = re.sub(r"[-+]", "", pnr)
    if len(digits) != 10:
        return False

    def luhn_checksum(num):
        total = 0
        for i, digit in enumerate(num):
            d = int(digit)
            if i % 2 == 0:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0

    return luhn_checksum(digits)

def score_ticket_components(ticket):
    components = {}

    required_fields = ['ticket_id', 'created_at', 'body']
    has_required = all(ticket.get(f) for f in required_fields)

    entity_values = ticket['entities'].values()
    num_filled_entities = sum(1 for v in entity_values if v is not None)
    total_entities = len(ticket['entities'])
    entity_completeness = num_filled_entities / total_entities if total_entities > 0 else 0

    components['completeness'] = 0.0 if not has_required else round(entity_completeness, 2)

    timestamp_ok = bool(re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}", ticket.get("created_at", "")))
    components['consistency'] = 1.0 if timestamp_ok else 0.0

    valid_ssn = validate_personnummer(ticket['entities'].get('personnummer')) if ticket['entities'].get('personnummer') else True
    valid_phone = bool(re.match(r"\+46\s?\d{1,3}[\s\d]+", ticket['entities'].get('phone', ''))) if ticket['entities'].get('phone') else True
    components['validity'] = 1.0 if valid_ssn and valid_phone else 0.0

    pii_found = any([
        ticket['entities'].get('personnummer'),
        ticket['entities'].get('phone'),
        ticket['entities'].get('email')
    ])
    components['privacy'] = 0.0 if pii_found else 1.0

    body = ticket.get("body", "").lower()
    lang_hint = ticket.get("lang_hint", "").lower()
    swedish_words = ['hej', 'får', 'kontoret', 'felkod', 'synkar']
    english_words = ['my', 'phone', 'friday', 'ssn']
    if lang_hint.startswith("sv"):
        match = any(w in body for w in swedish_words)
        lang_score = 1.0 if match else 0.0
    elif lang_hint.startswith("en"):
        match = any(w in body for w in english_words)
        lang_score = 1.0 if match else 0.0
    else:
        lang_score = 0.5
    components['language_match'] = lang_score

    components['quality_score'] = round(sum(components.values()) / len(components), 2)
    return components

