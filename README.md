**README**

**This project analyzes Swedish customer support tickets. It extracts structured information, calculates quality scores, redacts personal data, and serves the results through a REST API. It consists of two parts:**

1. **A Python script that processes the tickets and generates JSON reports.**
2. **A Java Spring Boot application that serves the processed data via a REST endpoint.**

## Summary

1. **Activate the Python virtual environment from inside ml_ticket_quality**

% source .venv/bin/activate

2. **Run the Python processing script**

% python main.py

This will generate ticket reports, redact sensitive data, and copy the scored report to the Java project folder.

3. **Navigate to the Java project directory**

% cd ../quality-api

4. **Start the Spring Boot server**

% mvn spring-boot:runy

5. **Access the API**
   **Open a browser or tool like Postman and go to:**

http://localhost:8080/v1/quality/summary

This returns the structured ticket report as JSON.

## 1. Project Structure

**Python part:**

* **Input file is located in the **data** folder.**
* **Output is saved in the **output** folder.**
* **All processing logic is inside the **src** folder.**
* **The main script is called **main.py**.**

**Java part:**

* **The Java backend is located in the **quality-api** or **java_quality_project** folder.**
* **The backend reads a JSON file called **quality_report.json** from the **src/main/resources** directory.**

## 2. Running the Python Script

1. **Activate a Python virtual environment.**

% source .venv/bin/activate

2. **From the root of the Python project, run the following command:**

% python main.py

**This will:**

* **Load input from:**

data/snippet.txt

* **Parse and clean ticket messages.**
* **Extract entities like customer ID, error code, action, and personal data.**
* **Compute quality scores (completeness, consistency, validity, privacy, language match).**
* **Redact any detected PII such as personnummer, phone numbers, and email addresses.**
* **Generate two output files:**

output/ticket_report_with_scores.json

output/ticket_report_redacted.json

* **Automatically copy the scored file to the Java backend as:**

../java_quality_project/src/main/resources/quality_report.json

**If the Java project has a different path, update this destination inside **main.py**.**

## 3. Running the Java REST API

1. **Ensure the file **quality_report.json** is present in:**

src/main/resources

2. **Open a terminal inside the Java project folder.**
3. **Start the Spring Boot application using Maven:**

% mvn spring-boot:run

4. **Once running, open the browser or API testing tool and go to:**

http://localhost:8080/v1/quality/summary

**This will return the full processed ticket report as JSON.**

## 4. Automated Bridge Between Python and Java

**After execution, the Python script copies the latest report directly into the Java backend directory:**

* **Source:**

output/ticket_report_with_scores.json

* **Destination:**

src/main/resources/quality_report.json

**This way, the Java backend always serves the most recent ticket data. No manual steps are required unless the folder names differ.**

## 5. Privacy and Redaction

**The Python script detects and redacts the following personal information from the ticket body:**

* **Swedish personal identity numbers (personnummer)**
* **Phone numbers**
* **Email addresses**

**A redacted version is saved separately and intended for safe sharing. Only cleaned data is exposed via the API. The original input is not stored long-term.**
