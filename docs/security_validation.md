# Nmap Scan Summary

---

## **Port 3000 – Node.js Express Framework (HTTP)**  
**Risk Level:**  Medium  

**Overview:**  
Port 3000 is typically used for local development environments, especially for Node.js applications. Exposing such environments to the internet poses risks, as they are often not configured with production-grade security.

**Recommended Mitigation:**  
- Ensure applications are production-ready with:
  - HTTPS enabled  
  - Rate limiting  
  - Proper input validation  
- Use a reverse proxy (e.g., **Nginx**, **Apache**) to manage and secure external traffic.

---

## **Port 5000 – Werkzeug HTTP Server (Python)**  
**Risk Level:**  Medium  

**Overview:**  
Werkzeug is a development server commonly used with Python frameworks like Flask. Its default settings lack essential production-grade security features such as encryption and concurrency handling.

**Recommended Mitigation:**  
- Do **not** use Werkzeug in production.  
- Deploy with a secure WSGI server (e.g., **Gunicorn**, **uWSGI**) behind a reverse proxy.  
- Restrict access to this port via firewall rules.

---

#  Burp Suite Scan Results

---

### 1. **Reflected Cross-Site Scripting (XSS)**  
**Severity:** High  

- **Vulnerability:** Unsanitized input in `q` parameter is reflected in the response.  
- **Example Request:** `GET /search?q=<script>alert(1)</script>`  
- **Risk:** Session hijacking, redirecting users, or running arbitrary scripts.

---

### 2. **Directory Listing Enabled**  
**Severity:**  Medium  

- **Location:** `http://127.0.0.1:3000/static/`  
- **Risk:** Reveals potentially sensitive files such as `.env` or config files.

---

### 3. **Missing Secure Cookie Attribute**  
**Severity:**  Medium  

- **Issue:** Cookies are set without the `Secure` flag.  
- **Example:** `Set-Cookie: sessionid=abc123; HttpOnly`  
- **Risk:** Interception over unencrypted channels.

---

### 4. **Server Version Disclosure**  
**Severity:** Low  

- **Header:** `Server: Werkzeug/3.1.3 Python/3.13.1`  
- **Risk:** Disclosed software versions can help attackers craft targeted exploits.

---

### 5. **Missing CSRF Protection**  
**Severity:**  Medium  

- **Endpoints Affected:** `/login`, `/register`  
- **Risk:** Allows malicious websites to perform unauthorized actions on behalf of users.

---

# OWASP ZAP Scan Results

---

##  **High Risk**

### 1. **Cross-Site Scripting (Reflected)**  
- **URL:** `http://127.0.0.1:3000/search?q=<script>alert(1)</script>`  
- **Description:** Input is not sanitized, allowing script injection.  
- **Solution:** Validate and sanitize all inputs; encode all output.

---

##  **Medium Risk**

### 2. **Insecure Cookies**  
- **URL:** `http://127.0.0.1:3000/`  
- **Description:** Cookies are sent without the `Secure` flag.  
- **Solution:** Add `Secure; HttpOnly; SameSite=Strict` attributes to all cookies.

---

### 3. **Missing CSRF Token**  
- **URL:** `http://127.0.0.1:3000/login`  
- **Description:** Forms lack CSRF protection.  
- **Solution:** Use anti-CSRF tokens for all state-changing forms.

---

## **Low Risk**

### 4. **Server Version Disclosure via HTTP Header**  
- **URL:** `http://127.0.0.1:3000/`  
- **Description:** Reveals server version: `Werkzeug/3.1.3 Python/3.13.1`  
- **Solution:** Suppress or replace the `Server` header.

---

### 5. **Directory Browsing**  
- **URL:** `http://127.0.0.1:3000/static/`  
- **Description:** Unrestricted access to directory contents.  
- **Solution:** Disable directory listing in your server configuration.

---

##  **Informational**

### 6. **X-Frame-Options Header Not Set**  
- **Risk:** May allow clickjacking attacks.  
- **Solution:** Set the header:  
  - `X-Frame-Options: DENY` **or**  
  - `X-Frame-Options: SAMEORIGIN`
