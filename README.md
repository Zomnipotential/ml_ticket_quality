1. Data Parsing

* The raw data from snippet.txt was parsed by detecting ticket_id as a marker and splitting ticket sections accordingly.
* Timestamps, channel, language hint, and message body were extracted using regex and structured into dictionaries.

2. Entity Extraction

* The body text was analyzed using regular expressions to extract:
  * customer_id (e.g., Kundnr 77821)
  * error_code (e.g., Felkod 504)
  * office_city (e.g., Malmö-kontoret)
  * action keywords (e.g., exporterar, synkar)
  * PII: personnummer, phone, email

3. PII Validation Checks

* Swedish SSNs (personnummer) were validated using the Luhn algorithm, which verifies the checksum of the final digit.
* Phone numbers were validated with a simplified E.164 format regex, ensuring they begin with +46 and contain valid digits/spaces.

* Quality Score Calculation
  Each ticket received a quality_score (0–1), composed of:

- Completeness: Percentage of extracted entities filled
- Consistency: Validity of the timestamp format (ISO 8601)
- Validity: Format checks on PII (SSN and phone)
- Privacy: Score penalized if PII is found (for GDPR safety)
- Language Match: Based on keywords in body vs lang_hint (sv or en)

5. Redaction

* SSNs, phone numbers, and emails were replaced using regex substitution with:
* [REDACTED SSN]
* [REDACTED PHONE]
* [REDACTED EMAIL]

6. Output

* Two final JSON files:
  * ticket_report_with_scores.json (entities + scores)
  * ticket_report_redacted.json (includes redacted body)
