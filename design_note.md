To deploy the system, I would run the Python script regularly, maybe using an automation tool. The Python code reads the raw tickets, extracts useful data, calculates quality scores, and saves the results to a JSON file. This file can then be used by the Java backend API, which reads it and returns the summary.

The backend could be deployed using simple tools like running the Spring Boot app on a server. If needed, it can be deployed to a cloud service like AWS for easier scaling. I would make sure the system can restart automatically if it crashes.

To monitor the system, I would log when tickets are processed and if something goes wrong (like missing fields or bad formatting). The logs can be printed to the console or saved to log files that I can check manually.

For GDPR, I made sure to redact sensitive information like Swedish personal numbers, phone numbers, and emails in the final output. This way, even if someone sees the report, they won’t see any private data. Also, I avoid saving the original input anywhere long-term, just the cleaned version.

Finally, I would make sure to explain in documentation how the system works, and who has access to what, so it’s clear how data is handled and kept safe.
