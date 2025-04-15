# Database Peer Review

**Tester**: Amanuel Bekele  
**Date**: 4/15/2025

---

## Connection Test
- **Task**: Connect to production database  
- **Result**: Pass

## Basic CRUD Test
- **Task**: Insert, read, update, delete test record  
- **Result**: Pass

## Critical Query Test
- **Task**: Run most important business query  
- **Subtask**: Verify results match expected output  
- **Result**: Pass

## Backup Verification
- **Task**: Confirm latest backup was completed successfully  
- **Result**: Pass

---

## Notes
No issues found.

-------------------------------------------------------------------------------------

# **Threat API – Peer Review**

## Overview
- **Reviewed Components:** Backend API, User Authentication Module, API KEYS TESTING
 **Reviewers:  Julius (Security)
 **Review Date:** April 15, 2025


  - **Code Optimization:** Consider optimizing the database queries in the user authentication module to reduce latency, especially for large datasets.
  - **Security:** Update the hashing mechanism for storing passwords to a stronger algorithm, such as bcrypt, instead of MD5.

### User Authentication Module
- **Bugs Identified:**
  - **Cross-Site Scripting (XSS):** The user registration form does not sanitize user input, which may allow XSS attacks. (Issue #46)
  - **Email Validation:** The system does not validate email format correctly; it allows invalid email formats to be submitted. (Issue #48)

- **Suggestions:**
  - Improve error handling on failed user registrations by providing specific error messages.
  - Add unit tests for edge cases in the authentication process, including account lockout after multiple failed login attempts.


#.
 **Improve email validation** logic (assigned to Steen).
 **Add unit tests** for edge cases in the authentication module (Tyler and Amanuel).
**Fix UI glitch** in the user profile dropdown (assigned to Tyler).

## Review Status
- **User Authentication Module:** Pending further revisions based on feedback. Issues with XSS and email validation need to be fixed.
- **Conduct testing of the API to ensure it is valid and set appropriate rate limits. 

-------------------------------------------------------------------------------------------

# **Threat Backend Server – Peer Review**

## Overview
- **Reviewed Components:** Backend Server
 **Reviewers:  Tyler 
 **Review Date:** April 15, 2025

---

## **1\. Security Issues**

### **Critical Concerns**

#### **Exposed Database Credentials**

* **Issue**: Database password and connection details are hardcoded in the source code.

* **Risk**: Source code access would compromise the database.

* **Recommendation**: Move credentials to environment variables or a secure secrets manager.

#### **Debug Mode in Production**

* **Issue**: `app.run(debug=True, port=5000)` enables debug mode.

* **Risk**: Exposes code and stack traces to users; allows remote code execution.

**Recommendation**: Use environment variables to control debug mode:

`app.run(debug=os.environ.get('DEBUG', 'False') == 'True')`


#### **File System Security**

* **Issue**: No access control for generated reports.

* **Risk**: Unauthorized access to sensitive information.

* **Recommendation**: Implement authentication and secure file storage.

---

### **Additional Security Concerns**

#### **SQL Injection Risk**

* **Issue**: Direct string concatenation in some queries.

* **Risk**: Potential SQL injection vulnerabilities.

* **Recommendation**: Use parameterized queries consistently.

#### **No Input Validation**

* **Issue**: Limited validation of incoming data.

* **Risk**: Malicious inputs could cause unexpected behavior.

* **Recommendation**: Validate all user inputs before processing.

---

## **2\. Performance Optimization**

### **Database Connection Management**

* **Issue**: A new connection is created for every request.

* **Risk**: Performance degradation and potential connection pool exhaustion.

* **Recommendation**: Implement connection pooling.

### **Missing Pagination**

* **Issue**: All endpoints return complete result sets.

* **Risk**: Performance issues with large datasets.

* **Recommendation**: Add limit/offset or cursor-based pagination.

### **Report Generation Efficiency**

* **Issue**: PDF generation is performed in-request.

* **Risk**: Request timeouts for large reports.

* **Recommendation**: Move report generation to background processing.

---

## **3\. Code Structure & Architecture**

### **Monolithic Design**

* **Issue**: All functionality resides in a single file.

* **Recommendation**: Split code into modules by function (e.g., routes, database, reports).

### **Error Handling Inconsistency**

* **Issue**: Inconsistent use of `try/except` blocks.

* **Recommendation**: Standardize error handling across all routes.

### **Duplicate Code**

* **Issue**: Repeated database operations across the codebase.

* **Recommendation**: Create utility functions for common operations.

### **Missing Documentation**

* **Issue**: Limited inline documentation.

* **Recommendation**: Add docstrings and API documentation throughout the codebase.

---

## **4\. Implementation Recommendations**

### **Database Access Layer (`db.py`)**


`import os`  
`import psycopg2`  
`from psycopg2.pool import ThreadedConnectionPool`

`# Load from environment variables`  
`DB_CONFIG = {`  
    `'dbname': os.environ.get('DB_NAME'),`  
    `'user': os.environ.get('DB_USER'),`  
    `'password': os.environ.get('DB_PASSWORD'),`  
    `'port': os.environ.get('DB_PORT'),`  
    `'host': os.environ.get('DB_HOST'),`  
    `'sslmode': 'require'`  
`}`

`# Connection pool`  
`pool = ThreadedConnectionPool(minconn=1, maxconn=10, **DB_CONFIG)`

`def get_connection():`  
    `return pool.getconn()`

`def release_connection(conn):`  
    `pool.putconn(conn)`

`def execute_query(query, params=None):`  
    `conn = get_connection()`  
    `try:`  
        `cursor = conn.cursor()`  
        `cursor.execute(query, params)`  
        `conn.commit()`  
        `cursor.close()`  
    `finally:`  
        `release_connection(conn)`

`def fetch_all(query, params=None):`  
    `conn = get_connection()`  
    `try:`  
        `cursor = conn.cursor()`  
        `cursor.execute(query, params)`  
        `results = cursor.fetchall()`  
        `cursor.close()`  
        `return results`  
    `finally:`  
        `release_connection(conn)`

---

### **Environment Configuration (`config.py`)**
  
`import os`  
`from dotenv import load_dotenv`

`load_dotenv()`

`# App configuration`  
`DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'`  
`PORT = int(os.environ.get('PORT', 5000))`  
`SECRET_KEY = os.environ.get('SECRET_KEY', 'generate-a-secure-key')`

`# File storage configuration`  
`REPORT_DIR = os.environ.get('REPORT_DIR', 'reports')`

---

### **Enhanced Security Implementation (`app.py`)**

`from flask_login import LoginManager, login_required`

`# Initialize login manager`  
`login_manager = LoginManager()`  
`login_manager.init_app(app)`

`# Protect routes requiring authentication`  
`@app.route('/api/generate-pdf-report', methods=['GET'])`  
`@login_required`  
`def generate_pdf_report():`  
    `# Existing PDF generation code`

---

### **Webhook Security (`app.py`)**

`import hmac`  
`import hashlib`

`@app.route('/webhook-handler', methods=['POST'])`  
`def handle_webhook():`  
    `signature = request.headers.get('X-Webhook-Signature')`  
    `secret = os.environ.get('WEBHOOK_SECRET')`

    `if not signature or not secret:`  
        `return jsonify({"error": "Unauthorized"}), 401`

    `payload = request.data`  
    `computed_signature = hmac.new(`  
        `secret.encode('utf-8'),`  
        `payload,`  
        `hashlib.sha256`  
    `).hexdigest()`

    `if not hmac.compare_digest(computed_signature, signature):`  
        `return jsonify({"error": "Invalid signature"}), 401`

    `# Process webhook data`  
    `data = request.json`  
    `# ...`

    `return jsonify({"status": "success"}), 200`

