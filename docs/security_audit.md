# Security Assessment Report

## Nmap Scan Summary

### Port 3000 – Node.js Express Framework (HTTP)
**Risk Level:** Medium  

**Description:**  
Port 3000 is commonly used for local development environments, particularly for Node.js apps. Exposing development environments externally increases the risk of attacks, as these environments may not be properly secured.

**Mitigation:**  
- Ensure that any Node.js app exposed to the internet is production-ready with proper security configurations (e.g., using HTTPS, rate limiting, input validation).  
- Implement a reverse proxy like Nginx or Apache to handle external requests securely.

---

### Port 5000 – Werkzeug HTTP Server (Python)
**Risk Level:** Medium  

**Description:**  
Werkzeug is often used as a development server for Python web applications (e.g., Flask). Running this server in production could expose the application to vulnerabilities due to its lack of advanced security features in the default configuration (e.g., lack of encryption, poor handling of concurrency).

**Mitigation:**  
- Avoid using Werkzeug in production; deploy applications with a production-ready WSGI server (e.g., Gunicorn, uWSGI) behind a reverse proxy (e.g., Nginx).  
- Ensure that access to this port is properly controlled using a firewall.

---

## Burp Suite Scan

### Vulnerabilities and Weaknesses

#### 1. Reflected XSS (**High Severity**)
**Description:**  
User-supplied input in the `q` parameter is reflected unsanitized in the response.

**Request Example:**  
`GET /search?q=<script>alert(1)</script>`

**Risk:**  
Can lead to session hijacking, redirecting users, or executing malicious scripts.

---

#### 2. Directory Listing Enabled (**Medium Severity**)  
**Location:** `http://127.0.0.1:3000/static/`  
**Description:**  
The server allows directory browsing, exposing files that may contain sensitive data (e.g., source code, .env, config files).

---

#### 3. Missing Secure Cookie Attribute (**Medium Severity**)  
**Observation:**  
The application sets cookies over HTTP without the `Secure` flag.

**Example:**  
`Set-Cookie: sessionid=abc123; HttpOnly`

**Risk:**  
Cookies can be intercepted over unencrypted connections.

---

#### 4. Server Version Disclosure (**Low Severity**)  
**Header:**  
`Server: Werkzeug/3.1.3 Python/3.13.1`

**Risk:**  
Attackers can use this information to craft targeted attacks if a vulnerability exists in the disclosed version.

---

#### 5. Missing CSRF Protection (**Medium Severity**)  
**Affected Endpoints:** `/login`, `/register`

**Description:**  
Critical forms do not include CSRF tokens to protect against cross-site request forgery.

**Risk:**  
An attacker could trick users into submitting unwanted requests.

---

## OWASP ZAP Scan

### High Risk

#### 1. Cross Site Scripting (Reflected)
- **Risk:** High  
- **URL:** `http://127.0.0.1:3000/search?q=<script>alert(1)</script>`  
- **Description:** The application does not sanitize user input in the `q` parameter, allowing arbitrary script execution.  
- **Solution:** Encode output, validate and sanitize input on both client and server sides.

---

### Medium Risk

#### 2. Cookie Without Secure Flag
- **Risk:** Medium  
- **URL:** `http://127.0.0.1:3000/`  
- **Description:** Cookies are transmitted over HTTP without the `Secure` flag, making them susceptible to interception.  
- **Solution:** Ensure all cookies include `Secure; HttpOnly; SameSite=Strict` attributes and serve them only over HTTPS.

#### 3. CSRF Token Missing
- **Risk:** Medium  
- **URL:** `http://127.0.0.1:3000/login`  
- **Description:** Login and other sensitive forms lack anti-CSRF tokens.  
- **Solution:** Implement CSRF tokens for all state-changing requests.

---

### Low Risk

#### 4. Server Leaks Information via “Server” HTTP Header
- **Risk:** Low  
- **URL:** `http://127.0.0.1:3000/`  
- **Description:** The server discloses its software and version: `Werkzeug/3.1.3 Python/3.13.1`.  
- **Solution:** Remove or obfuscate the Server header to minimize fingerprinting.

#### 5. Directory Browsing
- **Risk:** Low  
- **URL:** `http://127.0.0.1:3000/static/`  
- **Description:** The server allows directory listing, which could expose sensitive files.  
- **Solution:** Disable directory listing in your server configuration.

---

### Informational

#### 6. X-Frame-Options Header Not Set
- **Risk:** Informational  
- **Description:** This header can prevent clickjacking attacks.  
- **Solution:** Add the header `X-Frame-Options: DENY` or `SAMEORIGIN`.

---
